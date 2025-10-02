from flask import Blueprint

bp = Blueprint("feeds", __name__)

from . import routes  # noqa: E402,F401