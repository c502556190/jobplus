from flask import Flask
from flask_migrate import Migrate
from jobplus.models import db
from jobplus.config import configs


def register_extensions(app):
    db.init_app(app)
    Migrate(app, db)


def register_blueprints(app):
    from .handlers import admin, company, front, job, user
    app.register_blueprint(admin)
    app.register_blueprint(company)
    app.register_blueprint(front)
    app.register_blueprint(job)
    app.register_blueprint(user)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))

    register_extensions(app)
    register_blueprints(app)

    return app
