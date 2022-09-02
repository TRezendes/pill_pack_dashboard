from app import db
from sqlalchemy.dialects import sqlite3
from sqlalchemy import PrimaryKeyConstraint

class fill_lists(db.Model):
    list_export_name = db.Column(db.Text, primary _key=True)
    facility = db.Column(db.Text)
    exported = db.Column(db.Boolean)
    running = db.Column(db.Boolean)
    complete =  db.Column(db.Boolean)
