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
from .models import fill_lists
from ppd_flask import app, db
from config import basedir
from ppd_flask import db
from .forms import DotW, DotWlist
import csv
import os


fill_list_list = fill_lists.query.all()

@app.route('/')
def goToDashboard():
    return redirect(url_for('Dashboard'))

@app.route('/dashboard')
def Dashboard():
    return render_template(
        'dashboard.html',
        fill_list_list=fill_list_list
    )

@app.route('/reset', methods=['POST'])
def dbReset():
    #form='Reset'
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
    
@app.route('/settings')
def Settings():
    form = DotWlist
    return render_template(
        'settings.html',
        fill_list_list=fill_list_list,
        form=form
    )