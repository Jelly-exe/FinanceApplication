from flask import Blueprint, render_template, url_for, redirect, request, flash
from werkzeug.security import generate_password_hash, check_password_hash

from app.models import db
from app.models.user import User

register_bp = Blueprint("register", __name__)


@register_bp.route('/register')
def register():
    return render_template('auth/register.html')


@register_bp.route('/register', methods=['POST'])
def register_POST():
    username = request.form.get('username')
    name = request.form.get('name')
    password = request.form.get('password')
    confirmPassword = request.form.get('confirmPassword')

    user = User.query.filter_by(username=username).first()

    if user:
        flash("exists")
        return redirect(url_for('auth.register.register'))

    if password != confirmPassword:
        flash('Passwords do not match.')
        return redirect(url_for('auth.register.register'))

    new_user = User(username=username, name=name, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login.login'))
