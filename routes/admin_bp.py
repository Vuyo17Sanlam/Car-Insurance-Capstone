from flask import Blueprint, render_template, request

from extensions import db
from models.claims import Claim

admin_bp = Blueprint("admin_bp", __name__)


@admin_bp.get("/admin_dashboard")
def admin_page():
    return render_template("admin_dashboard.html")


@admin_bp.get("/admin_claims")
def admin_claims_page():
    claims = Claim.query.all()
    claim_dict = [claim.to_dict() for claim in claims]
    return render_template("admin_claims.html", claim_dict=claim_dict)


@admin_bp.get("/admin_user")
def admin_user_claims_page():
    claims = Claim.query.all()
    claim_dict = [claim.to_dict() for claim in claims]
    return render_template("admin_user.html", claim_dict=claim_dict)
