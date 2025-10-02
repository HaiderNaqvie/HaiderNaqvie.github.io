from __future__ import annotations

from flask import current_app


def is_ads_enabled() -> bool:
    client = current_app.config.get("ADSENSE_CLIENT_ID")
    return bool(client)
