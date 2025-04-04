import calendar
from collections import defaultdict
from datetime import datetime

from flask import Blueprint, render_template, request

from extensions import db
from models.claims import Claim
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
    # Fetch all users and build a lookup dictionary
    all_users = User.query.all()
    user_lookup = {user.user_id: user.user_name for user in all_users}

    # Fetch all claims
    claims = Claim.query.all()

    # Convert claims to dict and add user_name from lookup
    claim_dicts = []
    for claim in claims:
        claim_data = claim.to_dict()
        claim_data["user_name"] = user_lookup.get(claim.user_id, "Unknown")
        claim_dicts.append(claim_data)

    return render_template("admin_claims.html", claim_dict=claim_dicts)


@admin_bp.get("/admin_user")
def admin_user_claims_page():
    claims = Claim.query.all()
    claim_dict = [claim.to_dict() for claim in claims]
    return render_template("admin_user.html", claim_dict=claim_dict)
