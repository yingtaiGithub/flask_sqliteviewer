import ast
import pandas as pd

from app import app, db
from flask import render_template, request, redirect, url_for, flash, jsonify
from app.models import *
import sqlite3


def get_final_df(checked_areas, checked_regions):
    checked_allRegions = checked_regions + [row.region for area in checked_areas for row in Area_Region.query.filter_by(area=area)]

    cnx = sqlite3.connect(app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', ''))
    model_df = pd.read_sql_query("SELECT * FROM model", cnx)
    cache_df = pd.read_sql_query("SELECT * FROM cache", cnx)

    model_df_uncheckedRegions = model_df[~model_df['ORI_GEO_VAL'].isin(checked_allRegions)]
    cache_df_checkedRegions = cache_df[cache_df['ORI_GEO_VAL'].isin(checked_allRegions)]

    final_df = model_df_uncheckedRegions.append(cache_df_checkedRegions)

    return final_df

@app.route('/')
def home():
    """Render website's home page."""
    area_regions = [(x.area, x.region) for x in Area_Region.query.all()]
    values = sorted(set(map(lambda x:x[0], area_regions)))
    area_regions = [(x, set([y[1] for y in area_regions if y[0]==x])) for x in values]

    # cnx = sqlite3.connect(app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', ''))
    # final_df = pd.read_sql_query("SELECT * FROM final", cnx)
    # table = final_df.to_html(index=False)
    table = ''

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

    final_df = get_final_df(areas, regions)

    table = final_df.to_html(index=False)

    return jsonify(table)

@app.route("/restart")
def restart():
    area_rows = Status.query.filter_by(area=True)
    region_rows = Status.query.filter_by(area=False)

    areas = [row.name for row in area_rows]
    regions = [row.name for row in region_rows]

    final_df = get_final_df(areas, regions)
    table = final_df.to_html(index=False)

    data = {'areas': areas, 'regions': regions, 'table': table}

    return jsonify(data)

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404



