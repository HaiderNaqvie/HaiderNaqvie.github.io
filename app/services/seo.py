from __future__ import annotations

from typing import Any, Dict
from flask import request, current_app


def build_meta_context(
    *,
    title: str | None = None,
    description: str | None = None,
    og_image: str | None = None,
) -> Dict[str, Any]:
    site_url: str = current_app.config.get("SITE_URL", "")
    return {
        "title": title,
        "meta_description": description,
        "og_title": title,
        "og_description": description,
        "og_image": og_image or f"{site_url}/static/img/og-default.jpg",
        "canonical": f"{site_url}{request.path}",
    }
