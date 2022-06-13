import yaml
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.routes import auth_bp, view_bp
from app.models import db


def print_routes(app: Flask) -> None:
    for rule in app.url_map.iter_rules():
        print(rule)


def create_app():
    app = Flask(__name__)
    db.init_app(app)

    config = yaml.load(open("config.yml", "r"), Loader=yaml.FullLoader)

    app.config['SECRET_KEY'] = config["session-secret"]
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from app.models.user import User
        return User.query.get(int(user_id))

    app.register_blueprint(auth_bp)
    app.register_blueprint(view_bp)

    print_routes(app)
    return app
