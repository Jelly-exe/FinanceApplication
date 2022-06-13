from flask import Blueprint, render_template, url_for, request, flash, redirect
from werkzeug.security import check_password_hash
from flask_login import login_user, login_required, logout_user

from app.models.user import User

logout_bp = Blueprint("logout", __name__)


@logout_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login.login'))
