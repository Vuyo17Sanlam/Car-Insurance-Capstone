from constants import STATUS_CODE
from extensions import db
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from models.claims import Claim
from models.user import User
from werkzeug.security import check_password_hash, generate_password_hash

policy_bp = Blueprint("policy_bp", __name__)
