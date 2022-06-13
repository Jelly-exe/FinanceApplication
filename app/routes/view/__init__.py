from flask import Blueprint

view_bp = Blueprint("view", __name__)

from .overview import overview_bp
view_bp.register_blueprint(overview_bp)

# from .register import register_bp
# auth_bp.register_blueprint(register_bp)
#
# from .logout import logout_bp
# auth_bp.register_blueprint(logout_bp)

__all__ = ["view_bp"]
