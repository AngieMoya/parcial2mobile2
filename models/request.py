from config.db import  db, ma, app

class Request(db.Model):
    __tablename__ = "tblrequest"

    id = db.Column(db.Integer, primary_key =True)
    traveler = db.Column(db.Integer, ForeignKey('tbltraveler'))
    stop = db.Column(db.Integer, ForeignKey('tblstop'))
    origin_city = db.Column(db.Integer, ForeignKey('tblcity'))
    destiny_city = db.Column(db.Integer, ForeignKey('tblcity'))
    trip = db.Column(db.Integer, ForeignKey('tbltrip'))
    seats = db.Column(db.Integer(2))
    preferences = db.Column(db.String(100))

    def __init__(self, traveler, stop, origin_city, destiny_city, trip, seats, preferences):
        self. traveler = traveler
        self.stop = stop
        self.origin_city = origin_city
        self.destiny_city = destiny_city
        self.trip = trip
        self.seats = seats
        self.preferences = preferences

with app.app_context():
    db.create_all()

class RequestSchema(ma.Schema):
    class Meta:
        fields = ('id', 'traveler', 'stop', 'origin_city', 'destiny_city', 'trip', 'seats', 'preferences')