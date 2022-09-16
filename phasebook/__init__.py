from flask import Flask

from . import match, search, matchv2


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello World!"

    app.register_blueprint(match.bp)
    app.register_blueprint(matchv2.bp)
    app.register_blueprint(search.bp)

    return app
