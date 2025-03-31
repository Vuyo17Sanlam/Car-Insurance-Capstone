from flask import Blueprint, render_template, request

from extensions import db
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
def profile_page():
    return render_template("claims.html")


@user_bp.get("/claims_form")
def claim_forms():
    return render_template("claims_form.html")
