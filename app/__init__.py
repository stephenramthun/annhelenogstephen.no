from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
db.SQLALCHEMY_TRACK_MODIFICATIONS = True

from app import views, models
