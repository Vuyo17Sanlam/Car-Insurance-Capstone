from datetime import datetime, timedelta
from email import policy

import requests
from flask import Blueprint, flash, json, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from constants import STATUS_CODE
from extensions import db
from models.claims import Claim
from models.documents import Document
from models.policies import Policy
from models.user import User
from models.vehicles import Vehicles

user_bp = Blueprint("user_bp", __name__)


# API/Endpoint


@user_bp.get("/")
def get_home():
    return render_template("home.html")


@login_required
@user_bp.get("/dashboard")
def get_dashboard():
    # Get all policies for the current user
    policies = Policy.query.filter_by(user_id=current_user.user_id).all()

    all_vehicles = Vehicles.query.filter_by(user_id=current_user.user_id).all()
    vehicles_list = [
        # {**car.to_dict(), "car_image": get_car_image(car.make, car.model, car.year)}
        # for car in all_vehicles
        {
            **car.to_dict(),
            "car_image": "https://th.bing.com/th/id/OIP.ulEALEOzZVq-UvXKfp0HFAHaHk?rs=1&pid=ImgDetMain",
        }
        for car in all_vehicles
    ]

    # Calculate total premium
    total_premium = sum(float(policy.premium) for policy in policies)

    # Get today's date and monthly payment day from the first policy
    today = datetime.today()
    first_policy = policies[0] if policies else None
    day = (
        first_policy.monthly_payment_day if first_policy else 1
    )  # default to 1 if no policy

    # Calculate next month's payment date
    next_month = today.month + 1 if today.month < 12 else 1
    year = today.year if today.month < 12 else today.year + 1

    try:
        next_payment = datetime(year, next_month, day)
    except ValueError:
        next_payment = datetime(
            year, next_month, 28
        )  # fallback if day is invalid (e.g. Feb 30)

    # Format date as string
    next_month_date = next_payment.strftime("%B %d")

    # Fetch all users (if needed for the dashboard)
    users = User.query.all()
    users_dictionary = [user.to_dict() for user in users]

    return render_template(
        "dashboard.html",
        users=users_dictionary,
        total_premium=total_premium,
        next_month_date=next_month_date,
        vehicles_list=vehicles_list,
    )


@user_bp.get("/signup")
def signup_page():
    return render_template("signup.html")


@user_bp.post("/signup")
def submit_signup_page():
    try:
        # check if password and cofirm password match
        if request.form.get("password_hash") != request.form.get("confirm"):
            flash("Passwords do not match!", "danger")
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
        flash("Account created successfully!", "success")
        return redirect(url_for("user_bp.login_page"))
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


@login_required
@user_bp.get("/claims")
def claims_page():
    user_claims = Claim.query.filter_by(user_id=current_user.user_id).all()

    approved_claims = [
        claim for claim in user_claims if claim.claim_status == "Approved"
    ]
    pending_claims = [claim for claim in user_claims if claim.claim_status == "Pending"]
    rejected_claims = [
        claim for claim in user_claims if claim.claim_status == "Rejected"
    ]

    pending_num = len(pending_claims)
    approved_num = len(approved_claims)
    rejected_num = len(rejected_claims)

    return render_template(
        "claims.html",
        approved_claims=approved_claims,
        pending_claims=pending_claims,
        rejected_claims=rejected_claims,
        pending_num=pending_num,
        approved_num=approved_num,
        rejected_num=rejected_num,
    )


@user_bp.get("/claims_form")
def claim_forms():
    # Query the database for vehicles insured by the current user
    # vehicles = (
    #     db.session.query(Vehicles)
    #     .join(Policy)
    #     .filter(Policy.user_id == current_user.user_id)
    #     .all()
    # )
    all_vehicles = Vehicles.query.filter_by(user_id=current_user.user_id).all()
    vehicles_list = [
        # {**car.to_dict(), "car_image": get_car_image(car.make, car.model, car.year)}
        # for car in all_vehicles
        {
            **car.to_dict(),
            "car_image": "https://th.bing.com/th/id/OIP.ulEALEOzZVq-UvXKfp0HFAHaHk?rs=1&pid=ImgDetMain",
        }
        for car in all_vehicles
    ]

    return render_template("claims_form.html", vehicles_list=vehicles_list)


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


@user_bp.post("/claims")  # HOF
def submit_claim():
    vehicle_id = request.form.get("vehicle")
    print(vehicle_id)
    try:
        vehicle_id = request.form.get("vehicle")
        policy = Policy.query.filter_by(
            vehicle_id=vehicle_id,  # Fixed the typo here
        ).first()

        if not policy:
            flash("No active policy found for this vehicle", "error")
            return redirect(url_for("user_bp.claim_forms"))
        claim_data = {
            "policy_id": policy.policy_id,
            "user_id": current_user.user_id,
            "incident": request.form.get("incident"),
            "incident_date": request.form.get("incident_date"),
            "description": request.form.get("description"),
        }
        new_claim = Claim(**claim_data)
        db.session.add(new_claim)
        db.session.commit()

        police_report = request.form["police_report"]
        affidavit = request.form["affidavit"]
        images = request.form.getlist("images[]")

        # Convert list of image URLs to a JSON string
        count = 0
        images_json = {f"url{count + i}": str(img) for i, img in enumerate(images)}
        data = {
            "claim_id": new_claim.claim_id,
            "images": json.dumps(images_json),
            "affidavit": affidavit,
            "police_report": police_report,
        }

        # Create a new document instance
        new_document = Document(**data)
        db.session.add(new_document)
        db.session.commit()
        return redirect(url_for("user_bp.claims_page"))
    except Exception as e:
        print(e)
        db.session.rollback()  # Undo: Restore the data | After commit cannot undo
        return redirect(url_for("user_bp.claim_forms"))
    # data = {
    #     "name": users["name"],
    #     "dte": request.form.get("date"),
    #     "cause": request.form.get("cause"),
    #     "amount": users["amount"],
    #     "status": users["status"],
    # }
    # # data = request.get_json()  # body
    # new_claim = Claim(**data)

    # try:
    #     # print(new_movie, new_movie.to_dict())
    #     db.session.add(new_claim)
    #     db.session.commit()
    #     return redirect(url_for("user_bp.claims_page"))
    # except Exception as e:
    #     db.session.rollback()  # Undo: Restore the data | After commit cannot undo
    #     return {"message": str(e)}, STATUS_CODE["SERVER_ERROR"]


@user_bp.get("/partners")
def partners_page():
    return render_template("partners.html")


@user_bp.get("/insurance_form")
def insurance_form_page():
    return render_template("insurance_form.html")


# import xml.etree.ElementTree as ET

# import requests

# def get_car_image(make, model, year=None):
#     search_term = f"{make} {model} {year}" if year else f"{make} {model}"
#     url = f"http://www.carimagery.com/api.asmx/GetImageUrl?searchTerm={search_term.replace(' ', '+')}"

# response = requests.get(url)
# if response.status_code == 200:
#     root = ET.fromstring(response.content)
#     image_url = root.text
#     return image_url
# else:
#     return "failed to return the image"
