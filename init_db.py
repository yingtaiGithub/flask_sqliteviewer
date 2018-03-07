import sqlite3
import pandas as pd

from app.models import *
from app import db, app


def props(cls):
  return [i for i in cls.__dict__.keys() if i[:1] != '_']

def init_region_area():
    area = "ILSP"
    regions = ['IS26', 'IS08', 'IS22', 'IS04', 'IS20', 'IS07', 'IS14', 'IS12', 'IS18', 'IS16', 'IS11','IS06', 'IS02', 'IS10', 'IS09', 'IS24']
    area_regions = [(area, region) for region in regions ]
    for item in area_regions:
        area_region = Area_Region()
        area_region.area = item[0]
        area_region.region = item[1]

        db.session.add(area_region)

    db.session.commit()

def init_threadhold(input_csv):
    # data = [('NE18', 'NE18', 43),
    #         ('MT20', 'SE34', 45),
    #         ('MT22', 'IS02', 90)
    # ]
    # for item in data:
    #     threadhold = Threshold()
    #     threadhold.origin_region = item[0]
    #     threadhold.destination_region = item[1]
    #     threadhold.threshold = item[2]
    #
    #     db.session.add(threadhold)
    #
    # db.session.commit()

    df = pd.read_csv(input_csv)
    # print (df.columns)
    df['id'] = df['Unnamed: 0']
    df = df[['id', 'origin_area', 'origin_region', 'destination_area', 'threshold']]
    df.to_sql('threshold', cnx, if_exists='replace', index=False)

def init_offset(input_csv):
    # data = [('CATL', 'CATL', 43),
    #         ('DSW', 'FLA', 45),
    #         ('FLA', 'ILSP', 90)
    # ]
    # for item in data:
    #     offset = Offset()
    #     offset.origin_area = item[0]
    #     offset.destination_area = item[1]
    #     offset.offset = item[2]
    #
    #     db.session.add(offset)

    df = pd.read_csv(input_csv)
    df.rename(columns={'Unnamed: 0': 'id'}, inplace=True)

    df.to_sql('offset', cnx, if_exists='replace', index=False)


def init_cache(input_csv=None):
    # data = [('CATL', 'CATL', 'rstd', 10),
    #         ('DSW', 'FLA', 'normal', 11),
    #         ('FLA', 'ILSP', 'undershold', 14)
    # ]
    # for item in data:
    #     cache = CacheValue()
    #     cache.origin_area = item[0]
    #     cache.destination_area = item[1]
    #     cache.msi_origin = item[2]
    #     cache.cache_value = item[3]
    #
    #     db.session.add(cache)
    #
    # db.session.commit()

    df = pd.read_csv(input_csv)
    df.rename(columns={'Unnamed: 0': 'id'}, inplace=True)

    df.to_sql('cache_value', cnx, if_exists='replace', index=False)


if __name__ == "__main__":
    pass
    cnx = sqlite3.connect(app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', ''))
    db.create_all()
    # init_region_area()
    # init_threadhold('threshold.csv')
    # init_offset('offset.csv')
    # init_cache('cache.csv')
