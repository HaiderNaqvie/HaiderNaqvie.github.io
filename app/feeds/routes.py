from __future__ import annotations

from datetime import datetime
from flask import Response
from sqlalchemy import select

from app.extensions import db
from app.models import Post

from . import bp


@bp.route("/feed.xml")
def feed():
    posts = (
        db.session.execute(
            select(Post).where(Post.status == "published").order_by(Post.published_at.desc()).limit(30)
        )
        .scalars()
        .all()
    )
    items = []
    for p in posts:
        items.append(
            f"""
            <item>
              <title>{p.title}</title>
              <link>/blogs/{p.slug}</link>
              <pubDate>{(p.published_at or p.created_at).strftime('%a, %d %b %Y %H:%M:%S +0000')}</pubDate>
              <description><![CDATA[{p.excerpt or ''}]]></description>
            </item>
            """
        )
    xml = f"""
    <rss version="2.0">
      <channel>
        <title>Latest Posts</title>
        <link>/</link>
        <description>Recent posts</description>
        <lastBuildDate>{datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S +0000')}</lastBuildDate>
        {''.join(items)}
      </channel>
    </rss>
    """
    return Response(xml, mimetype="application/rss+xml")
