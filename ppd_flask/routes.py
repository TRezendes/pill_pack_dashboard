from ppd_flask import app, db
from flask import render_template, redirect, url_for, flash, request
from .models import fill_lists
import csv
import os



@app.route('/')
def goToDashboard():
    return redirect(url_for('Dashboard'))

@app.route('/dashboard')
def Dashboard():
    fill_list_list = fill_lists.query.all()
    return render_template(
        'dashboard.html',
        fill_list_list=fill_list_list
    )

@app.route('/reset', methods=['POST'])
def dbReset():
    form='Reset'
    if request.method == 'POST':
        fill_lists.query.delete()
        db.session.commit()
        fac_obj_list=[]
        print('**************************************')
        print(os.path.abspath(url_for('static', filename="facilities.csv")))
        with open('/static/facilities.csv', newline='') as f:
            reader = csv.reader(f)
            facilityList = list(reader)

        for facility in facilityList:
            fac_dict = {'list_export_name': facility[0],'display_name': facility[1],'facility': facility[2]}
            fac_obj = fill_lists(**fac_dict)
            fac_obj_list.append(fac_obj)
        db.session.add_all(fac_obj_list)
        db.session.commit()
    return redirect(url_for('Dashboard'))
