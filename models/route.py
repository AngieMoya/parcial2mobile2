from config.db import  db, ma, app

class Route(db.Model):
    __tablename__= "routes"

    id = db.Column(db.Integer, primary_key =True)
    origin = db.Column(db.Integer, ForeignKey('cities'))
    destination = db.Column(db.Integer, ForeignKey('cities'))
    distance = db.Column(db.Integer(9))

    def __init__(self, origin, destination, distance):
        self.origin = origin
        self.destination = destination
        self.distance = distance

with app.app_context():
    db.create_all()

class RouteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'origin', 'destination', 'distance')
