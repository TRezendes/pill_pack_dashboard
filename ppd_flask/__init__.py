from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from config import Config


app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = Config.SECRET_KEY
app = Flask(__name__)
db = SQLAlchemy(app)
from ppd import routes