from datetime import datetime

from constants import STATUS_CODE
from extensions import db
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from flask_login import current_user, login_required, login_user, logout_user
from models.policies import Policy
from models.user import User
from models.vehicles import Vehicles

car_insurance_bp = Blueprint("car_insurance_bp", __name__)


@car_insurance_bp.get("/insurance_form")
def insurance_form_page():
    return render_template("insurance_form.html")


@car_insurance_bp.post("/insurance_form")
def submit_vehicle_details():
    if not current_user.is_authenticated:
        flash("You need to be logged in to submit a policy.")
        return redirect(url_for("user_bp.login_page"))

    try:
        data = {
            "make": request.form.get("make"),
            "model": request.form.get("model"),
            "year": request.form.get("year"),
            "vin": request.form.get("vin"),
            "license_plate": request.form.get("license_plate"),
            "current_mileage": request.form.get("current_mileage"),
            "purchase_date": request.form.get("purchase_date"),
            "estimated_current_value": request.form.get("estimated_current_value"),
            "user_id": current_user.user_id,
        }

        new_vehicle = Vehicles(**data)
        db.session.add(new_vehicle)
        db.session.commit()

        # Extract policy data from the form
        coverage_type = request.form["coverage_type"]

        # Determine the premium amount based on coverage type
        if coverage_type == "comprehensive":
            premium_amount = 2000
        elif coverage_type == "third-party":
            premium_amount = 3000
        elif coverage_type == "third-party-fire-theft":
            premium_amount = 4000

        # Create a new policy
        pol_data = {
            "user_id": current_user.user_id,
            "vehicle_id": new_vehicle.vehicle_id,
            "start_date": datetime.now(),
            "premium": premium_amount,
            "coverage_type": coverage_type,
        }
        new_policy = Policy(**pol_data)
        db.session.add(new_policy)
        db.session.commit()

        return redirect(url_for("user_bp.get_dashboard"))
    except Exception as e:
        print(e)
        db.session.rollback()  # Undo: Restore the data | After commit cannot undo

        return redirect(url_for("car_insurance_bp.insurance_form_page"))
