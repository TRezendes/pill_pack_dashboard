from ppd_flask import db

class fill_lists(db.Model):
    list_export_name = db.Column(db.Text, primary_key=True)
    display_name = db.Column(db.Text, nullable=False, unique=True)
    facility = db.Column(db.Text)
    exported = db.Column(db.Boolean, default=False)
    running = db.Column(db.Boolean, default=False)
    complete =  db.Column(db.Boolean, default=False)
