import calendar
import json
from collections import defaultdict
from datetime import datetime

from flask import Blueprint, render_template, request

from extensions import db
from models.claims import Claim
from models.documents import Document
from models.policies import Policy
from models.user import User

admin_bp = Blueprint("admin_bp", __name__)


@admin_bp.get("/admin_dashboard")
def admin_page():
    all_users = User.query.all()
    user_dict = [all_user.to_dict() for all_user in all_users]
    user_list = list(user_dict)
    no_user = len(user_list)

    # Get all claims
    claims = Claim.query.all()

    # Initialize all months with 0
    monthly_counts = {month: 0 for month in calendar.month_abbr[1:]}  # Jan to Dec

    status_counts = {"pending": 0, "approved": 0, "rejected": 0}

    for claim in claims:
        if claim.incident_date:
            month_str = calendar.month_abbr[claim.incident_date.month]  # e.g. "Jan"
            monthly_counts[month_str] += 1

        # Count statuses (case-insensitive)
        status = claim.claim_status.lower()
        if status in status_counts:
            status_counts[status] += 1

    # Convert dict to list of (month, count) in calendar order
    ordered_months = list(calendar.month_abbr[1:])  # Jan to Dec
    monthly_data = [[month, monthly_counts[month]] for month in ordered_months]

    return render_template(
        "admin_dashboard.html",
        monthly_counts=monthly_data,
        status_counts=status_counts,
        no_user=no_user,
    )


@admin_bp.get("/admin_claims")
def admin_claims_page():
    all_users = User.query.all()
    user_lookup = {user.user_id: user.user_name for user in all_users}

    claims = Claim.query.all()
    claim_dicts = []
    for claim in claims:
        claim_data = claim.to_dict()
        claim_data["user_name"] = user_lookup.get(claim.user_id, "Unknown")
        claim_dicts.append(claim_data)

    return render_template("admin_claims.html", claim_dict=claim_dicts)


@admin_bp.route("/admin_user/<claim_id>")
def admin_user_claims_page(claim_id):
    # Fetch the claim
    claim = Claim.query.filter_by(claim_id=claim_id).first()

    if not claim:
        return "Claim not found", 404

    # Fetch related user, policy, and documents
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

    # Pass data to the template
    return render_template(
        "admin_user.html",
        claim=claim,
        user=user,
        policy=policy,
        document=document,
        images=images,
    )
