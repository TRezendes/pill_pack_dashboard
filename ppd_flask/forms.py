from ppd_flask import db
from flask_wtf import FlaskForm
from ppd_flask.models import fill_lists
from wtforms.validators import Optional
from wtforms.validators import DataRequired
from wtforms import FieldList, HiddenField, SelectField

class DotW(FlaskForm):
    days = [(1,'Monday'),(2,'Tuesday'),(3,'Wednesday'),(4,'Thursday'),(5,'Friday'),(6,'Saturday'),(7,'Sunday')]
    pull_day = SelectField('Pull Day', choices=days, coerce=int, allow_blank=True, blank_text="Day", validators=[(Optional())])
    fill_day = SelectField('Fill Day', choices=days, coerce=int, allow_blank=True, blank_text="Day", validators=[(Optional())])
    del_day = SelectField('Delivery Day', choices=days, coerce=int, allow_blank=True, blank_text="Day", validators=[(Optional())])

class DotWlist(FlaskForm):
    settings = FieldList(DotW)