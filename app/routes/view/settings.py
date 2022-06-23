import yaml
from flask import Blueprint, render_template, redirect, url_for

from utils import get_balance, get_transactions, getDates
from flask_login import login_required, current_user

settings_bp = Blueprint("settings", __name__)
config = yaml.load(open("config.yml", "r"), Loader=yaml.FullLoader)


@settings_bp.route('/settings')
@login_required
def settings():
    return render_template('view/settings.html',
                           sfe_1st={"amount": 3000,
                                    "date": "some date 1"},
                           sfe_2nd={"amount": 3000,
                                    "date": "some date 2"},
                           sfe_3rd={"amount": 3000,
                                    "date": "some date 3"},
                           getDates=getDates
                           )
