from __future__ import annotations

from flask import render_template, request
from sqlalchemy import select

from app.extensions import db
from app.models import Post

from . import bp


@bp.route("/")
def search():
    q = (request.args.get("q") or "").strip()
    posts = []
    if q:
        stmt = (
            select(Post)
            .where(Post.status == "published")
            .where(Post.title.ilike(f"%{q}%") | Post.excerpt.ilike(f"%{q}%"))
            .order_by(Post.published_at.desc().nullslast())
            .limit(50)
        )
        posts = db.session.execute(stmt).scalars().all()
    return render_template("search/results.html", q=q, posts=posts)