from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from constants import STATUS_CODE
from extensions import db
from models.claims import Claim
from models.user import User

user_bp = Blueprint("user_bp", __name__)


# API/Endpoint


@user_bp.get("/")
def get_home():
    return render_template("home.html")


@login_required
@user_bp.get("/dashboard")
def get_dashboard():
    users = User.query.all()
    users_dictionary = [user.to_dict() for user in users]
    return render_template("dashboard.html", users=users_dictionary)


@user_bp.get("/signup")
def signup_page():
    return render_template("signup.html")


@user_bp.post("/signup")
def submit_signup_page():
    try:
        # check if password and cofirm password match
        if request.form.get("password_hash") != request.form.get("confirm"):
            raise ValueError("Password does not match")

        password = request.form.get("password_hash")
        hashed_password = generate_password_hash(password)  # 16 -> salt length
        data = {
            "user_name": request.form.get("user_name"),
            "password_hash": hashed_password,
            "surname": request.form.get("surname"),
            "id_number": request.form.get("id_number"),
            "dob": request.form.get("dob"),
            "gender": request.form.get("gender"),
            "email": request.form.get("email"),
            "phone_no": request.form.get("phone_no"),
            "address": request.form.get("address"),
            "title": request.form.get("title"),
        }
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("user_bp.insurance_form_page"))
    except Exception as e:
        db.session.rollback()  # Undo: Restore the data | After commit cannot undo
        print(str(e))
        return redirect(url_for("user_bp.signup_page"))


@user_bp.get("/login")
def login_page():
    return render_template("login.html")


@user_bp.post("/login")
def submit_login_page():
    user_name = request.form.get("user_name")
    password_hash = request.form.get("password_hash")
    try:
        # 🛡️ Validations
        if not user_name:
            raise ValueError("Username must be filled")

        if not password_hash:
            raise ValueError("Password must be filled")

        user_from_db = User.query.filter_by(user_name=user_name).first()

        print(user_from_db)

        if not user_from_db:
            raise ValueError("Credentials are invalid")

        if not check_password_hash(user_from_db.password_hash, password_hash):
            raise ValueError("Credentials are invalid")
        login_user(user_from_db)
        flash("Login successful", "success")
        return redirect(url_for("user_bp.get_dashboard"))

    except Exception as e:
        print(e)
        db.session.rollback()
        flash(str(e), "danger")
        return redirect(url_for("user_bp.submit_login_page"))


@user_bp.get("/logout")
def logout_page():
    logout_user()
    return redirect(url_for("user_bp.submit_login_page"))


@user_bp.get("/claims")
def claims_page():
    users = User.query.all()
    users_dictionary = [user.to_dict() for user in users]
    return render_template("claims.html", users=users_dictionary)


@user_bp.get("/claims_form")
def claim_forms():
    users = User.query.all()
    users_dictionary = [user.to_dict() for user in users]
    return render_template("claims_form.html", user=users_dictionary)


@user_bp.get("/support")
def user_support():
    return render_template("support.html")


@user_bp.get("/partners")
def partners():
    return render_template("partners.html")


@user_bp.get("/new")
def add_claim_page():
    return render_template("claims_form.html")


# usrs = {"name": "Inga", "amount": 10_000, "status": "pending"}


@user_bp.post("/")  # HOF
def create_claim():
    data = {
        "name": users["name"],
        "dte": request.form.get("date"),
        "cause": request.form.get("cause"),
        "amount": users["amount"],
        "status": users["status"],
    }
    # data = request.get_json()  # body
    new_claim = Claim(**data)

    try:
        # print(new_movie, new_movie.to_dict())
        db.session.add(new_claim)
        db.session.commit()
        return redirect(url_for("user_bp.claims_page"))
    except Exception as e:
        db.session.rollback()  # Undo: Restore the data | After commit cannot undo
        return {"message": str(e)}, STATUS_CODE["SERVER_ERROR"]


@user_bp.get("/partners")
def partners_page():
    return render_template("partners.html")
