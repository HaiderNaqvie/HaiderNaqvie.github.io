from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
from flask_wtf import CSRFProtect
from flask_compress import Compress


db = SQLAlchemy()
migrate = Migrate()
cache = Cache()
csrf = CSRFProtect()
compress = Compress()


def init_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
    csrf.init_app(app)
    compress.init_app(app)
