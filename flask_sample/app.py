from flask import Flask
from .database import init_db
import flask_sample.models


def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_sample.config.Config')

    init_db(app)

    return app

app = create_app()

@app.route("/",methods=["GET"])
def register_page():
    return 