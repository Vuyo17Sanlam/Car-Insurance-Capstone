from constants import STATUS_CODE
from extensions import db
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from flask_login import current_user, login_required, login_user, logout_user
from models.user import User
from models.vehicles import Vehicles
from werkzeug.security import check_password_hash, generate_password_hash

car_insurance_bp = Blueprint("car_insurance_bp", __name__)


@car_insurance_bp.get("/insurance_form")
def insurance_form_page():
    return render_template("insurance_form.html")


@car_insurance_bp.post("/insurance_form")
def submit_vehicle_details():
    print("hey")
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

        # Print the data to debug
        print(data)

        new_vehicle = Vehicles(**data)
        db.session.add(new_vehicle)
        db.session.commit()
        return redirect(url_for("user_bp.login_page"))
    except Exception as e:
        db.session.rollback()  # Undo: Restore the data | After commit cannot undo
        print(str(e))
        return redirect(url_for("car_insurance_bp.insurance_form_page"))
