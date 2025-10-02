import os
from flask import Flask

try:
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except Exception:
    # dotenv is optional in production
    pass

from .extensions import init_extensions


def create_app(config_object: str | None = None) -> Flask:
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_folder="static",
        template_folder="templates",
    )

    # Config
    if config_object:
        app.config.from_object(config_object)
    else:
        env = os.environ.get("FLASK_ENV", "development").lower()
        if env.startswith("prod"):
            app.config.from_object("config.ProductionConfig")
        elif env.startswith("test"):
            app.config.from_object("config.TestingConfig")
        else:
            app.config.from_object("config.DevelopmentConfig")

    # Ensure instance folder exists for SQLite, uploads, etc.
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass

    # Extensions
    init_extensions(app)

    # Ensure models are imported so migrations can detect them
    from . import models  # noqa: F401

    # Blueprints
    from .main import bp as main_bp
    app.register_blueprint(main_bp)
    # Additional blueprints (registered later when implemented)
    try:
        from .blog import bp as blog_bp
        app.register_blueprint(blog_bp, url_prefix="/blogs")
    except Exception:
        pass
    try:
        from .sitemaps import bp as sitemaps_bp
        app.register_blueprint(sitemaps_bp)
    except Exception:
        pass
    try:
        from .category import bp as category_bp
        app.register_blueprint(category_bp, url_prefix="/category")
    except Exception:
        pass
    try:
        from .feeds import bp as feed_bp
        app.register_blueprint(feed_bp)
    except Exception:
        pass
    try:
        from .search import bp as search_bp
        app.register_blueprint(search_bp, url_prefix="/search")
    except Exception:
        pass
    try:
        from .pages import bp as pages_bp
        app.register_blueprint(pages_bp)
    except Exception:
        pass

    # Template globals
    @app.context_processor
    def inject_site_info():
        return {
            "SITE_NAME": app.config.get("SITE_NAME", "TrendSphere"),
            "SITE_URL": app.config.get("SITE_URL", "http://localhost:5000"),
        }

    # Security headers
    @app.after_request
    def apply_security_headers(response):
        response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("X-Frame-Options", "SAMEORIGIN")
        response.headers.setdefault("X-XSS-Protection", "0")
        if response.status_code == 404:
            response.headers.setdefault("Cache-Control", "public, max-age=60")
        else:
            response.headers.setdefault("Cache-Control", "public, max-age=300")
        return response

    return app
