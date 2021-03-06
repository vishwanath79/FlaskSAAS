from flask import Flask

from snakeeyes.blueprints.page import views
from snakeeyes.extensions import debug_toolbar

def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    #app.register_blueprint(page)
    app.register_blueprint(views.page)

    return app

def extensions(app):
    """
    Register 0 or more extensions
    :param app:
    :return:
    """
    debug_toolbar.init_app(app)
    return None

