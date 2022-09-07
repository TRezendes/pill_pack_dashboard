import csv
from ppd_flask import db
from ppd_flask.models import *

db.create_all()

fill_lists.query.delete()
db.session.commit()
fac_obj_list=[]
with open('ppd_flask/static/facilities.csv', newline='') as f:
    reader = csv.reader(f)
    facilityList = list(reader)
    
for facility in facilityList:
    fac_dict = {'list_export_name': facility[0],'display_name': facility[1],'facility': facility[2]}
    fac_obj = fill_lists(**fac_dict)
    fac_obj_list.append(fac_obj)
db.session.add_all(fac_obj_list)
db.session.commit()