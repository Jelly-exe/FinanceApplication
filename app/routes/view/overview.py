import yaml
from flask import Blueprint, render_template, redirect, url_for

from utils import get_balance, get_transactions
from flask_login import login_required, current_user

overview_bp = Blueprint("overview", __name__)
config = yaml.load(open("config.yml", "r"), Loader=yaml.FullLoader)


@overview_bp.route('/')
@login_required
def index():
    return redirect(url_for('auth.login.login'))


@overview_bp.route('/overview')
@login_required
def overview():
    balance = get_balance(config["personal-access-token"])
    transactions = get_transactions(config["personal-access-token"], 30, 15)

    weekly_amount = 80
    weekly_left = 60

    sfe_total = 9000
    sfe_1st = 3000
    sfe_2nd = 3000
    sfe_3rd = 3000

    accommodation_total = 6000
    accommodation_1st = 2000
    accommodation_2nd = 2000
    accommodation_3rd = 2000

    return render_template('view/overview.html',
                           balance=balance,
                           weekly_amount=weekly_amount,
                           weekly_left=weekly_left,
                           sfe_total=sfe_total,
                           sfe_1st=sfe_1st,
                           sfe_2nd=sfe_2nd,
                           sfe_3rd=sfe_3rd,
                           transactions=transactions,
                           accommodation_total=accommodation_total,
                           accommodation_1st=accommodation_1st,
                           accommodation_2nd=accommodation_2nd,
                           accommodation_3rd=accommodation_3rd)


@overview_bp.route('/oldoverview')
def oldoverview():
    balance = get_balance(config["personal-access-token"])
    transactions = get_transactions(config["personal-access-token"], 30, 15)

    weekly_amount = 80
    weekly_left = 60

    sfe_total = 9000
    sfe_1st = 3000
    sfe_2nd = 3000
    sfe_3rd = 3000

    accommodation_total = 6000
    accommodation_1st = 2000
    accommodation_2nd = 2000
    accommodation_3rd = 2000

    return render_template('old/overview.html',
                           balance=balance,
                           weekly_amount=weekly_amount,
                           weekly_left=weekly_left,
                           sfe_total=sfe_total,
                           sfe_1st=sfe_1st,
                           sfe_2nd=sfe_2nd,
                           sfe_3rd=sfe_3rd,
                           transactions=transactions,
                           accommodation_total=accommodation_total,
                           accommodation_1st=accommodation_1st,
                           accommodation_2nd=accommodation_2nd,
                           accommodation_3rd=accommodation_3rd)
