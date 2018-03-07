import ast
import pandas as pd

from app import app, db
from flask import render_template, request, redirect, url_for, flash, jsonify
from app.models import *
import sqlite3

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    area_regions = [(x.area, x.region) for x in Area_Region.query.all()]
    values = sorted(set(map(lambda x:x[0], area_regions)))
    area_regions = [(x, set([y[1] for y in area_regions if y[0]==x])) for x in values]

    cnx = sqlite3.connect(app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', ''))
    final_df = pd.read_sql_query("SELECT * FROM final", cnx)
    table = final_df.to_html(index=False)

    return render_template('home.html', area_regions=area_regions, table=table)

@app.route("/submit")
def submit():
    areas = request.args.get('areas', None)
    regions = request.args.get("regions", None)

    areas = ast.literal_eval(areas)
    regions = ast.literal_eval(regions)

    area_rows = [Status(area, True) for area in areas]
    region_rows =[Status(region, False) for region in regions]

    rows = area_rows + region_rows

    Status.query.delete()
    db.session.add_all(rows)
    db.session.commit()

    print (areas)
    print (regions)

    return "Success"

@app.route("/get_status")
def get_status():
    area_rows = Status.query.filter_by(area=True)
    region_rows = Status.query.filter_by(area=False)

    areas = [row.name for row in area_rows]
    regions = [row.name for row in region_rows]

    data = {'areas': areas, 'regions': regions}

    return jsonify(data)


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404



