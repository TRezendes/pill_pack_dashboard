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
        with open('../facilities.csv', newline='') as f:
            reader = csv.reader(f)
            facilityList = list(reader)
        
        for facility in facilityList:
            fill_list = fill_lists(
                list_export_name=facility[0],
                display_name=facility[1],
                facility=facility[2]
            )
            db.session.add(fill_list)
            db.session.commit()
    return redirect(url_for('Dashboard'))
