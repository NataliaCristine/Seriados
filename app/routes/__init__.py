from flask import Flask
from app.routes.series_blueprint import bp_series


def init_app(app:Flask):
    app.register_blueprint(bp_series)