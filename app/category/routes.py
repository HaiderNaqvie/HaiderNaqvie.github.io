from __future__ import annotations

from flask import abort, render_template
from sqlalchemy import select

from app.extensions import db
from app.models import Category, Post

from . import bp


@bp.route("/<slug>")
def by_category(slug: str):
    category = db.session.execute(select(Category).where(Category.slug == slug)).scalar_one_or_none()
    if not category:
        abort(404)
    posts = (
        db.session.execute(
            select(Post)
            .where(Post.category_id == category.id, Post.status == "published")
            .order_by(Post.published_at.desc().nullslast())
            .limit(24)
        )
        .scalars()
        .all()
    )
    return render_template("category/list.html", category=category, posts=posts)
