from config.db import  db, ma, app

class Trip(db.Model):
    __tablename__ = "tbltrip"

    id = db.Column(db.Integer, primary_key =True)
    vehicle = db.Column(db.Integer, ForeignKey('tblvehicle'))
    route = db.Column(db.Integer, ForeignKey('tblroute'))
    start_time = db.Column(db.String(50))
    ending_time = db.Column(db.String(50))

    def __init__(self, vehicle, route, start_time, ending_time):
        self.vehicle = vehicle
        self.route = route
        self.start_time = start_time
        self.ending_time = ending_time

with app.app_context():
    db.create_all()

class TripSchema(ma.Schema):
    class Meta:
        fields = ('id', 'vehicle', 'route', 'start_time', 'ending_time')