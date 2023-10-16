from config.db import  db, ma, app

class Request(db.Model):
    __tablename__ = "requests"

    id = db.Column(db.Integer, primary_key =True)
    traveler = db.Column(db.Integer, db.ForeignKey('travelers.id'))
    stop = db.Column(db.Integer, db.ForeignKey('stops.id'))
    origin_city = db.Column(db.Integer, db.ForeignKey('cities.id'))
    destiny_city = db.Column(db.Integer, db.ForeignKey('cities.id'))
    trip = db.Column(db.Integer, db.ForeignKey('trips.id'))
    seats = db.Column(db.Integer())
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