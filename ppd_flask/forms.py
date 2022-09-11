from ppd_flask import db
from flask_wtf import FlaskForm, Form
from ppd_flask.models import Facility, FillList
from wtforms.validators import DataRequired, Optional
from wtforms import FieldList, FormField, HiddenField, SelectField

class DotW(Form):
    days = [(0,'Day of Week…'),(1,'Monday'),(2,'Tuesday'),(3,'Wednesday'),(4,'Thursday'),(5,'Friday'),(6,'Saturday'),(7,'Sunday')]
    pull_day = SelectField('Pull Day', choices=days, coerce=int, validators=[(Optional())])
    fill_day = SelectField('Fill Day', choices=days, coerce=int, validators=[(Optional())])
    del_day = SelectField('Delivery Day', choices=days, coerce=int, validators=[(Optional())])

class DotWlist(FlaskForm):
    settings = FieldList(FormField(DotW), min_entries=1)