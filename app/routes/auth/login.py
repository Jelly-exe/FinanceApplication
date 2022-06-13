from flask import Blueprint, render_template, url_for, request, flash, redirect
from werkzeug.security import check_password_hash
from flask_login import login_user, current_user

from app.models.user import User

login_bp = Blueprint("login", __name__)


@login_bp.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('view.overview.overview'))

    return render_template('auth/login.html')


@login_bp.route('/login', methods=['POST'])
def login_POST():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login.login'))

    login_user(user, remember=remember)
    return redirect(url_for('view.overview.overview'))
