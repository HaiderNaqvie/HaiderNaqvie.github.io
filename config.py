import os


class BaseConfig:
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-this-in-production")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///blog.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Caching
    CACHE_TYPE = os.environ.get("CACHE_TYPE", "SimpleCache")
    CACHE_DEFAULT_TIMEOUT = int(os.environ.get("CACHE_DEFAULT_TIMEOUT", "300"))

    # Site
    SITE_NAME = os.environ.get("SITE_NAME", "TrendSphere")
    SITE_URL = os.environ.get("SITE_URL", "http://localhost:5000")
    PER_PAGE = int(os.environ.get("PER_PAGE", "12"))

    # Analytics / Monetization (optional)
    GA_ID = os.environ.get("GA_ID", "")
    ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    ENV = "development"


class ProductionConfig(BaseConfig):
    DEBUG = False
    ENV = "production"
    PROPAGATE_EXCEPTIONS = False


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
