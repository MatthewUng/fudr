from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Group(db.Model):
    __tablename__ = "groups"

    name = db.Column(db.String, primary_key=True)
    url = db.Column(db.String)
    restaurants = db.relationship('Restaurant', backref='owner_group')

    def __init__(self, name, url):
        print('creating group')
        self.name = name
        self.url = url
        print(self.name, self.url)

class Restaurant(db.Model):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String)
    image = db.Column(db.String)
    count = db.Column(db.Integer, default=0)
    group_id = db.Column(db.String, db.ForeignKey('groups.name'))

    def __init__(self, name, url, image):
        self.name = name
        self.url = url
        self.image = image