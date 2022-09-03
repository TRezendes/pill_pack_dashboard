from ppd import app
from flask import render_template, redirect, url_for, flash, request
from ppd.models import fill_lists

listOfLists = [
    ['LA_1st.dat', 'LA 1', 'Lakeview'],
    ['LA_2nd.dat', 'LA 2', 'Lakeview'],
    ['LA_3rd.dat', 'LA 3', 'Lakeview'],
    ['LA_4th.dat', 'LA 4', 'Lakeview'],
    ['RidgeA.dat', 'Ridge A', 'Tel Hai Skilled'],
    ['RidgeB.dat', 'Ridge B', 'Tel Hai Skilled'],
    ['RidgeC.dat', 'Ridge C', 'Tel Hai Skilled'],
    ['BrookA.dat', 'Brook A', 'Tel Hai Skilled'],
    ['BrookB.dat', 'Brook B', 'Tel Hai Skilled'],
    ['BrookC.dat', 'Brook C', 'Tel Hai Skilled'],
    ['Memory_Support.dat', 'LV', 'Meadowview'],
    ['MtnView_Upper.dat', 'MV Upper', 'Mountainview Upper'],
    ['MtnView_Lower.dat', 'MV Lower', 'Mountainview Lower'],
    ['GSV_Skilled_FC.dat', 'FC', 'GSV Skilled'],
    ['GSV_Skilled_WG.dat', 'WG', 'GSV Skilled'],
    ['GSV_Skilled_SW.dat', 'SW', 'GSV Skilled'],
    ['GSV_Skilled_SF.dat', 'SF', 'GSV Skilled'],
    ['FMT_Farmcrest.dat', 'FA', 'Farmcrest'],
    ['FMT_WRPC.dat', 'PC', 'WRPC'],
    ['FMT_NE_NF.dat', 'NE, NF', 'FMT Skilled'],
    ['FMT_NG_NH.dat', 'NG, NH', 'FMT Skilled']
]

@app.route('/')
def goToDashboard:
    return redirect(url_for('Dashboard'))
    
@app.route('/dashboard')
def Dashboard:
    return render_template('dashboard.html')
    
@app.route('/reset')
def dbReset:
    if form.validate_on_submit():
        for list in listOfLists:
            fill_list = fill_lists(
                list_export_name=list[0],
                display_name=list[1],
                facility=list[2]
            )
            db.session.add(fill_list)
            db.session.commit()
    return redirect(url_for('Dashboard'))
