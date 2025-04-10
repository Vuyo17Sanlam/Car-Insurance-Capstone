import calendar
import json
from collections import defaultdict
from datetime import datetime

from flask import Blueprint, redirect, render_template, request, url_for

from extensions import db
from models.claims import Claim
from models.documents import Document
from models.policies import Policy
from models.recent_activity import RecentActivity
from models.user import User

admin_bp = Blueprint("admin_bp", __name__)


@admin_bp.get("/admin_dashboard")
def admin_page():
    all_users = User.query.all()
    user_dict = [all_user.to_dict() for all_user in all_users]
    user_list = list(user_dict)
    no_user = len(user_list)

    all_activities = RecentActivity.query.limit(3).all()
    all_activities_dict = [act.to_dict() for act in all_activities]

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
    try:
        if "approve" in request.form:
            claim.claim_status = "Approved"
        elif "reject" in request.form:
            claim.claim_status = "Rejected"
        else:
            return "No action specified", 400

        db.session.commit()  # Save changes to DB
        return redirect(
            url_for("admin_bp.admin_claims_page")
        )  # Redirect to avoid resubmission
    except Exception as e:
        print(e)
        db.session.rollback()  # Undo changes on error
        return f"Error updating claim: {str(e)}", 500
