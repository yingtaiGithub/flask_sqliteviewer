from app import db

class Area_Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(20))
    region = db.Column(db.String(20))


    # def __repr__(self):
    #     return '<User %r>' % self.name

class Threshold(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin_area = db.Column(db.String(20))
    origin_region = db.Column(db.String(20))
    destination_area = db.Column(db.String(20))
    threshold = db.Column(db.Integer())

class Offset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin_area = db.Column(db.String(20))
    destination_area = db.Column(db.String(20))
    offset = db.Column(db.Integer)

class CacheValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin_area = db.Column(db.String(20))
    destination_area = db.Column(db.String(20))
    msi_origin = db.Column(db.String(20))
    cache = db.Column(db.Integer)

class Final(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    origin_area = db.Column(db.String(20))
    origin_region = db.Column(db.String(20))
    destination_area = db.Column(db.String(20))
    msi_origin = db.Column(db.String(20))
    final = db.Column(db.Integer)
    cache = db.Column(db.Integer)



