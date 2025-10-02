from flask import Blueprint

bp = Blueprint("category", __name__)

from . import routes  # noqa: E402,F401
