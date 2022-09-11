'''
MIT License

Copyright (c) 2022 Timothy Rezendes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from ppd_flask import db
from sqlalchemy import CheckConstraint

class FillList(db.Model):
    list_export_name = db.Column(db.Text, primary_key=True)
    display_name = db.Column(db.Text, nullable=False, unique=True)
    facility = db.Column(db.Text, nullable=False)
    exported = db.Column(db.Boolean, default=False, nullable=False)
    running = db.Column(db.Boolean, default=False, nullable=False)
    complete =  db.Column(db.Boolean, default=False, nullable=False)
    
class Facility(db.Model):
    facility_name = db.Column(db.Text, primary_key=True)
    pull_day = db.Column('pull_day', db.Integer, db.CheckConstraint('pull_day BETWEEN 0 AND 7'), default=0, nullable=False)
    fill_day = db.Column('fill_day', db.Integer, db.CheckConstraint('pull_day BETWEEN 0 AND 7'), default=0, nullable=False)
    del_day = db.Column('del_day', db.Integer, db.CheckConstraint('pull_day BETWEEN 0 AND 7'), default=0, nullable=False)