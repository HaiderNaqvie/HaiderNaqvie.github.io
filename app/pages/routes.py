from __future__ import annotations

from flask import render_template, abort
from sqlalchemy import select

from app.extensions import db
from app.models import Page

from . import bp


@bp.route("/<slug>")
def simple_page(slug: str):
    # reserved slugs
    if slug in {"about", "contact", "privacy", "terms"}:
        return render_template(f"pages/{slug}.html")

    page = db.session.execute(select(Page).where(Page.slug == slug)).scalar_one_or_none()
    if not page:
        abort(404)
    return render_template("pages/generic.html", page=page)
