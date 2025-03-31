from extensions import db
from flask import Blueprint, render_template, request
from models.claims import Claim
from models.user import User

user_bp = Blueprint("user_bp", __name__)


# API/Endpoint


@user_bp.get("/")
def get_movies():
    users = User.query.all()
    users_dictionary = [user.to_dict() for user in users]
    return render_template("dashboard.html", users=users_dictionary)
