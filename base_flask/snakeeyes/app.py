from flask import Flask


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True) #inform,s flask to look for an instance module which is at snakeeyes module

    app.config.from_object('config.settings') #loads config.settings module
    app.config.from_pyfile('settings.py', silent=True) #loads py file inside the instance folder (instance/settngs),siltent tells flask not to crash if file does not exist

    @app.route('/')
    def index():
        """
        Render a Hello World response.

        :return: Flask response
        """
        return app.config['HELLO']

    return app
