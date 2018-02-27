from app.models import *
from app import db

def init_region_area():
    region_area = [('CATL', 'NE18'), ('CATL', 'NE18'), ('DSW', 'MT20'), ('DSW', 'MT22'), ('FLA', 'SE34'), ('FLA', 'SE36'), ('ILSP', 'IS02'), ('ILSP', 'IS04')]
    for item in region_area:
        area_region = Area_Region()
        area_region.area = item[0]
        area_region.region = item[1]

        db.session.add(area_region)

    db.session.commit()

def init_threadhold():
    data = [('NE18', 'NE18', 43),
            ('MT20', 'SE34', 45),
            ('MT22', 'IS02', 90)
    ]
    for item in data:
        threadhold = Threshold()
        threadhold.origin_region = item[0]
        threadhold.destination_region = item[1]
        threadhold.threshold = item[2]

        db.session.add(threadhold)

    db.session.commit()

def init_offset():
    data = [('CATL', 'CATL', 43),
            ('DSW', 'FLA', 45),
            ('FLA', 'ILSP', 90)
    ]
    for item in data:
        offset = Offset()
        offset.origin_area = item[0]
        offset.destination_area = item[1]
        offset.offset = item[2]

        db.session.add(offset)

def init_cache():
    data = [('CATL', 'CATL', 'rstd', 10),
            ('DSW', 'FLA', 'normal', 11),
            ('FLA', 'ILSP', 'undershold', 14)
    ]
    for item in data:
        cache = CacheValue()
        cache.origin_area = item[0]
        cache.destination_area = item[1]
        cache.msi_origin = item[2]
        cache.cache_value = item[3]

        db.session.add(cache)

    db.session.commit()

if __name__ == "__main__":
    # init_region_area()
    # init_threadhold()
    # init_offset()
    init_cache()
