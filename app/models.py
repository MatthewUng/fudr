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
    group_id = db.Column(db.String, db.ForeignKey('groups.name'))

    def __init__(self, name, url):
        self.name = name
        self.url = url