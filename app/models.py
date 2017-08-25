from . import db

class Group(db.Model):
    __tablename__ = "groups"

    name = db.Column(db.String, primary_key=True)
    restaurants = db.relationship('Restaurant', backref='owner_group')

    def __init__(self, name):
        self.name = name

class Restaurant(db.Model):
    __tablename__ = "restaurants"

    name = db.Column(db.String, primary_key=True)
    url = db.Column(db.String)
    image = db.Column(db.String)
    count = db.Column(db.Integer, default=0)
    group_id = db.Column(db.String, db.ForeignKey('groups.name'))

    def __init__(self, name, url, image):
        self.name = name
        self.url = url
        self.image = image