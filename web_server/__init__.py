from flask import Flask
from pymongo import MongoClient

MONGO_URI = "mongodb+srv://gon:2025@cluster0.sm3ik1j.mongodb.net/?retryWrites=true&w=majority" # for using cloud
# MONGO_URI = "mongodb://localhost:27017/" # for using local storage
CLIENT = MongoClient(MONGO_URI)
DB = CLIENT['myweb'].board


def create_app():
    app = Flask(__name__)

    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app


# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Hell py"

