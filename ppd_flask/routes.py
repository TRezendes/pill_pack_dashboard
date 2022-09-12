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

from ppd_flask.models import facility as Facility, fill_list as FillList
from flask import render_template, redirect, url_for, flash, request
from ppd_flask.forms import DotW, DotWlist
from sqlalchemy import update
from ppd_flask import app, db
from config import basedir
import csv
import os



@app.route('/')
def goToDashboard():
    return redirect(url_for('Dashboard'))

@app.route('/dashboard')
def Dashboard():
    fill_list_list = FillList.query.all()
    return render_template(
        'dashboard.html',
        fill_list_list=fill_list_list
    )

@app.route('/rebuild', methods=['POST'])
def dbRebuild():
    facilityFilePath=os.path.join(basedir, 'ppd_flask/static', 'facilities.csv')
    if request.method == 'POST':
        tables = db.metadata.tables.keys()
        if 'facility' in tables:
            Facility.query.delete()
        if 'fill_list' in tables:
            FillList.query.delete()
        db.session.commit()
        fac_list=[]
        fac_obj_list=[]
        fl_obj_list=[]
        with open(facilityFilePath, newline='') as f:
            reader = csv.reader(f)
            facilityList = list(reader)
        for facility in facilityList:
            fac_dit = {'facility_name': facility[2]}
            if facility[2] not in fac_list:
                fac_list.append(facility[2])
                fac_obj = Facility(**fac_dit)
                fac_obj_list.append(fac_obj)
            fl_dict = {'list_export_name': facility[0],'display_name': facility[1], 'facility': facility[2]}
            fl_obj = FillList(**fl_dict)
            fl_obj_list.append(fl_obj)
        db.session.add_all(fac_obj_list)
        db.session.add_all(fl_obj_list)
        db.session.commit()
    return redirect(url_for('Dashboard'))
    
@app.route('/reset', methods=['POST'])
def dbReset():
    update(FillList).values(exported=False, running=False, completed=False)
    return redirect(url_for('Dashboard'))
    
@app.route('/settings', methods=['GET', 'POST'])
def Settings():
    facility_list = Facility.query.all()
    form = DotWlist()
    print(facility_list)
    # print(fac_name_list)
    return render_template(
        'settings.html',
        facility_list=facility_list,
        # fac_name_list=fac_name_list,
        form=form
    )
    
