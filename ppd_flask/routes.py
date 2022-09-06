from ppd import app
from flask import render_template, redirect, url_for, flash, request
from ppd.models import fill_lists
import csv



@app.route('/')
def goToDashboard:
    return redirect(url_for('Dashboard'))

@app.route('/dashboard')
def Dashboard:
    return render_template('dashboard.html')

@app.route('/reset')
def dbReset:
    if form.validate_on_submit():
        fill_lists.query.delete()
        db.session.commit()
        with open('../facilities.csv', newline='') as f:
            reader = csv.reader(f)
            facilityList = list(reader)

        for facility in facilityList:
            fac_dict = {
            'list_export_name': facility[0],
            'display_name': facility[1],
            'facility': facility[2]
            }
            fac_obj = fill_lists(**fac_dict)
            fac_obj_list.append(fac_obj)
        db.session.add_all(fac_obj_list)
        db.session.commit()
    return redirect(url_for('Dashboard'))
