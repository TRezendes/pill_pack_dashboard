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

from flask import render_template, redirect, url_for, flash, request
from datetime import datetime, timedelta
from ppd_flask.models import fill_lists
from ppd_flask import app, db
from config import basedir
import csv
import os

def timeTier(export_time):
    now=datetime.now()
    then=now-timedelta(0,60)
    if export_time.date() == now.date():
        if export_time > then:
            display_class = 'Tier1'
        else:
            display_class = 'Tier2'
    else:
        display_class = 'Tier3'
    return display_class

@app.route('/')
def goToDashboard():
    return redirect(url_for('Dashboard'))

@app.route('/dashboard')
def Dashboard():
    fill_list_list = fill_lists.query.all()
    fill_list_dict = {}
    sub_key1 = 'display_name'
    sub_key2 = 'facility'
    sub_key3 = 'exported'
    sub_key4 = 'display_class'
    for fill_list in fill_list_list:
        key = fill_list.list_export_name
        attribute_dict = {
        sub_key1: fill_list.display_name,
        sub_key2: fill_list.facility,
        sub_key3: fill_list.exported,
        sub_key4: timeTier(fill_list.last_export)
        }
        fill_list_dict[key] = attribute_dict
    return render_template(
        'dashboard.html',
        fill_list_list=fill_list_list,
        fill_list_dict=fill_list_dict
    )

@app.route('/reset', methods=['POST'])
def dbReset():
    form='Reset'
    facilityFilePath=os.path.join(basedir, 'ppd_flask/static', 'facilities.csv')
    if request.method == 'POST':
        fill_lists.query.delete()
        db.session.commit()
        fac_obj_list=[]
        with open(facilityFilePath, newline='') as f:
            reader = csv.reader(f)
            facilityList = list(reader)

        for facility in facilityList:
            fac_dict = {'list_export_name': facility[0],'display_name': facility[1],'facility': facility[2]}
            fac_obj = fill_lists(**fac_dict)
            fac_obj_list.append(fac_obj)
        db.session.add_all(fac_obj_list)
        db.session.commit()
    return redirect(url_for('Dashboard'))
