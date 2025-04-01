from flask import Blueprint, redirect, render_template, request, url_for

from constants import STATUS_CODE
from extensions import db
from models.claims import Claim
from models.user import User

user_bp = Blueprint("user_bp", __name__)


# API/Endpoint


@user_bp.get("/")
def get_dashboard():
    users = User.query.all()
    users_dictionary = [user.to_dict() for user in users]
    return render_template("dashboard.html", users=users_dictionary)


@user_bp.get("/dashboard")
def get_dashboard_after():
    users = User.query.all()
    users_dictionary = [user.to_dict() for user in users]
    return render_template("dashboard.html", users=users_dictionary)


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


@user_bp.get("/new")
def add_claim_page():
    return render_template("claims_form.html")


usrs = {"name": "Inga", "amount": 10_000, "status": "pending"}


@user_bp.post("/")  # HOF
def create_claim():
    data = {
        "name": usrs["name"],
        "dte": request.form.get("date"),
        "cause": request.form.get("cause"),
        "amount": usrs["amount"],
        "status": usrs["status"],
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
