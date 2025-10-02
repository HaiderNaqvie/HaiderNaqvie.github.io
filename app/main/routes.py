from __future__ import annotations

from flask import render_template, send_from_directory, current_app

from . import bp
from app.services.cache import cached_section


@cached_section(timeout=60)
def _sample_posts() -> list[dict]:
    return [
        {
            "title": "AI Trends to Watch in 2025",
            "snippet": "From multimodal agents to edge inference, here are the trends...",
            "thumbnail": "https://picsum.photos/seed/ai2025/600/400",
            "filename": "ai-trends-2025",
        },
        {
            "title": "Budget Travel Guide: 10 Countries Under $50/day",
            "snippet": "Stretch your dollars further with these destinations and tips...",
            "thumbnail": "https://picsum.photos/seed/travel/600/400",
            "filename": "budget-travel-10-countries",
        },
        {
            "title": "Morning Routines Backed by Science",
            "snippet": "Small habits that compound into big health wins...",
            "thumbnail": "https://picsum.photos/seed/health/600/400",
            "filename": "morning-routines-science",
        },
    ]


@bp.route("/")
def index():
    featured = _sample_posts()
    recent = _sample_posts() + _sample_posts()
    trending = _sample_posts()
    return render_template("home.html", featured=featured, recent=recent, trending=trending)


@bp.route("/robots.txt")
def robots_txt():
    return send_from_directory(current_app.static_folder, "robots.txt", mimetype="text/plain")


@bp.route("/ads.txt")
def ads_txt():
    return send_from_directory(current_app.static_folder, "ads.txt", mimetype="text/plain")
