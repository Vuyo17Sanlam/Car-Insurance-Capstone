import calendar
import json
import uuid
from collections import defaultdict
from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from extensions import db
from models import recent_activity
from models.claims import Claim
from models.documents import Document
from models.policies import Policy
from models.recent_activity import RecentActivity
from models.user import User

admin_bp = Blueprint("admin_bp", __name__)


@admin_bp.get("/admin_login")
def admin_login_page():
    return render_template("admin_login.html")


@admin_bp.get("/admin_logout")
def logout_page():
    logout_user()
    return redirect(url_for("admin_bp.submit_admin_login_page"))


@admin_bp.post("/admin_login")
def submit_admin_login_page():
    id_number = request.form.get("id_number", "").strip()
    password_hash = request.form.get("password_hash", "").strip()

    try:
        # Validations
        if not id_number:
            raise ValueError("ID number is required")

        if not password_hash:
            raise ValueError("Password is required")

        if int(id_number) != 5555555555555:
            raise ValueError("Credentials are invalid")

        user_from_db = User.query.filter_by(id_number=id_number).first()

        print(user_from_db)

        if not user_from_db:
            raise ValueError("Credentials are invalid")

        if not check_password_hash(user_from_db.password_hash, password_hash):
            raise ValueError("Credentials are invalid")
        login_user(user_from_db)
        flash("Login successful", "success")
        return redirect(url_for("admin_bp.admin_page"))

    except Exception as e:
        print(e)
        db.session.rollback()
        flash(str(e), "danger")
        return redirect(url_for("admin_bp.submit_admin_login_page"))


@admin_bp.get("/admin_dashboard")
def admin_page():
    all_users = User.query.all()
    user_dict = [all_user.to_dict() for all_user in all_users]
    user_list = list(user_dict)
    no_user = len(user_list)

    last_three = (
        RecentActivity.query.order_by(RecentActivity.created_at.desc())
        .limit(3)
        .all()[::-1]
    )

    all_activities_dict = [act.to_dict() for act in last_three]

    claims = Claim.query.all()

    monthly_counts = {month: 0 for month in calendar.month_abbr[1:]}

    status_counts = {"pending": 0, "approved": 0, "rejected": 0}

    for claim in claims:
        if claim.incident_date:
            month_str = calendar.month_abbr[claim.incident_date.month]
            monthly_counts[month_str] += 1

        status = claim.claim_status.lower()
        if status in status_counts:
            status_counts[status] += 1

    ordered_months = list(calendar.month_abbr[1:])
    monthly_data = [[month, monthly_counts[month]] for month in ordered_months]

    return render_template(
        "admin_dashboard.html",
        monthly_counts=monthly_data,
        status_counts=status_counts,
        no_user=no_user,
        all_activities_dict=all_activities_dict,
    )


@admin_bp.get("/admin_claims")
def admin_claims_page():
    all_users = User.query.all()
    user_lookup = {user.user_id: user.user_name for user in all_users}
    user_lookup1 = {user.user_id: user.surname for user in all_users}

    claims = Claim.query.all()
    claim_dicts = []
    for claim in claims:
        claim_data = claim.to_dict()
        claim_data["user_name"] = user_lookup.get(claim.user_id, "Unknown")
        claim_data["surname"] = user_lookup1.get(claim.user_id, "Unknown")
        claim_dicts.append(claim_data)

    return render_template("admin_claims.html", claim_dict=claim_dicts)


@admin_bp.get("/admin_user/<claim_id>")
def admin_user_claims_page(claim_id):
    claim = Claim.query.filter_by(claim_id=claim_id).first()

    if not claim:
        return "Claim not found", 404

    user = User.query.filter_by(user_id=claim.user_id).first()
    policy = Policy.query.filter_by(policy_id=claim.policy_id).first()
    document = Document.query.filter_by(claim_id=claim.claim_id).first()

    images = []
    if document and document.images:
        try:
            image_dict = json.loads(document.images)
            images = list(image_dict.values())
        except Exception as e:
            print("Error parsing images JSON:", e)

    return render_template(
        "admin_user.html",
        claim=claim,
        user=user,
        policy=policy,
        document=document,
        images=images,
    )


# @admin_bp.post("/admin_user/<claim_id>")
# def update_claim_status(claim_id):
#     claim_id = request.form["claim_id"]
#     new_status = request.form["status"]


#     claim = Claim.query.filter_by(claim_id=claim_id).first()
#     if claim:
#         claim.claim_status = new_status
#         db.session.commit()
#     return redirect(url_for("admin_bp.update_claim_status", claim_id=claim_id))
@admin_bp.post("/admin_user/<claim_id>")
def update_claim_status(claim_id):
    claim = Claim.query.filter_by(claim_id=claim_id).first()

    if not claim:
        return "Claim not found", 404

    try:
        # Create a new recent activity instance
        new_activity = RecentActivity()
        new_activity.id = uuid.uuid4()

        if "approve" in request.form:
            claim.claim_status = "Approved"
            new_activity.activity = f"Admin approved claim {claim_id}"
            new_activity.created_at = datetime.utcnow()

        elif "reject" in request.form:
            claim.claim_status = "Rejected"
            new_activity.activity = f"Admin rejected claim {claim_id}"
            new_activity.created_at = datetime.utcnow()

        else:
            return "No action specified", 400

        # Add the recent activity to the session
        db.session.add(new_activity)
        db.session.commit()  # Save all changes
        return redirect(url_for("admin_bp.admin_claims_page"))

    except Exception as e:
        print(e)
        db.session.rollback()
        return f"Error updating claim: {str(e)}", 500
