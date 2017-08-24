from . import db

class Group(db.Model):
    __tablename__ = "groups"

    name = db.Column(db.String, primary_key=True)
    place_1 = db.Column(db.String)
    url_1 = db.Column(db.String)
    place_2 = db.Column(db.String)
    url_2 = db.Column(db.String)
    place_3 = db.Column(db.String)
    url_3 = db.Column(db.String)

    def __init__(self, name, d1, d2, d3):
        self.name = name
        self.places = db.relationship("Restaurant")
        # self.place_1, self.url_1 = d1['name'], d1['url']
        # self.place_2, self.url_2 = d2['name'], d2['url']
        # self.place_3, self.url_3 = d3['name'], d3['url']

class Restaurant(db.Model):
    __tablename__ = "restaurants"

    name = db.Column(db.String, primary_key=True)
    url = db.Column(db.String)

    def __init__(self, name, url):
        self.name = name
        self.url = url