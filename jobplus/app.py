from flask import Flask
from jobplus.config import configs


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

    register_blueprints(app)

    return app
