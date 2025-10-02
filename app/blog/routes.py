from __future__ import annotations

from flask import abort, render_template
from sqlalchemy import select

from app.extensions import db
from app.models import Post

from . import bp


@bp.route("/")
def list_posts():
    stmt = (
        select(Post)
        .where(Post.status == "published")
        .order_by(Post.published_at.desc().nullslast())
        .limit(24)
    )
    posts = db.session.execute(stmt).scalars().all()
    return render_template("blog/list.html", posts=posts)


@bp.route("/<slug>")
def detail(slug: str):
    stmt = select(Post).where(Post.slug == slug, Post.status == "published").limit(1)
    post = db.session.execute(stmt).scalar_one_or_none()
    if not post:
        abort(404)
    return render_template("blog/detail.html", post=post)
