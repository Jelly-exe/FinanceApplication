from flask import Blueprint

from .overview import overview_bp
from .settings import settings_bp

view_bp = Blueprint("view", __name__)

view_bp.register_blueprint(overview_bp)
view_bp.register_blueprint(settings_bp)

__all__ = ["view_bp"]
