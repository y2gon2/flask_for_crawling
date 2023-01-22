from flask import Flask
from pymongo import MongoClient

MONGO_URI = "mongodb+srv://gon:2025@cluster0.sm3ik1j.mongodb.net/?retryWrites=true&w=majority"
CLIENT = MongoClient(MONGO_URI)
DB = CLIENT['myweb'].board

# def conn_mongodb():
#     db = CLIENT.myweb
#     test = db.test_connection.insert_one({'first': 'test'})
#     return db

# conn_mongodb()

def create_app():
    app = Flask(__name__)

    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app


# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Hell py"

