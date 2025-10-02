from __future__ import annotations

from datetime import datetime
from flask import Response, current_app
from sqlalchemy import select

from app.extensions import db
from app.models import Post, Category, Page

from . import bp


@bp.route("/sitemap.xml")
def sitemap_xml():
    site_url: str = current_app.config.get("SITE_URL", "")
    urls: list[str] = []

    # Static pages
    urls += ["/", "/blogs/", "/feed.xml", "/about", "/contact", "/privacy", "/terms"]

    # Dynamic posts
    posts = db.session.execute(select(Post).where(Post.status == "published")).scalars().all()
    urls += [f"/blogs/{p.slug}" for p in posts]

    # Categories
    categories = db.session.execute(select(Category)).scalars().all()
    urls += [f"/category/{c.slug}" for c in categories]

    # Pages
    pages = db.session.execute(select(Page)).scalars().all()
    urls += [f"/{p.slug}" for p in pages]

    lastmod = datetime.utcnow().strftime("%Y-%m-%d")
    parts = [
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>",
        "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">",
    ]
    for path in urls:
        parts.append(
            f"<url><loc>{site_url}{path}</loc><lastmod>{lastmod}</lastmod><changefreq>daily</changefreq></url>"
        )
    parts.append("</urlset>")
    return Response("".join(parts), mimetype="application/xml")
