import sqlite3
import pandas as pd

from app import app
from app.models import *

def get_area(row):

    row['origin_area'] = Area_Region.query.filter_by(region=str(row.origin_region)).first().area
    row['destination_area'] = Area_Region.query.filter_by(region=str(row.destination_region)).first().area

    return row


def main():
    cnx = sqlite3.connect(app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', ''))

    thread_df = pd.read_sql_query("SELECT * FROM threshold", cnx)
    thread_df = thread_df.drop(['id'], axis=1)
    thread_df = thread_df.apply(get_area, axis=1)

    offset_df = pd.read_sql_query("SELECT * FROM offset", cnx)
    offset_df = offset_df.drop(['id'], axis=1)


    cache_df = pd.read_sql_query("SELECT * FROM cache_value", cnx)
    cache_df = cache_df.drop(['id'], axis=1)

    offset_cache_df = pd.merge(offset_df, cache_df, how='outer', on=['origin_area', 'destination_area'])

    final_df = pd.merge(thread_df, offset_cache_df, how='left', on=['origin_area', 'destination_area'])
    final_df = final_df.dropna()
    final_df['final'] = final_df['offset'] + final_df['threshold']
    final_df = final_df[['origin_area', 'origin_region', 'destination_area', 'destination_region', 'msi_origin', 'final', 'cache_value']]

    final_df.to_sql('final', cnx, if_exists='replace', index=False)

if __name__ == "__main__":
    main()