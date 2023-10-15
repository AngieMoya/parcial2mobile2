from config.db import  db, ma, app

class Vehicle(db.Model):
    __tablename__ = "vehicles"

    id = db.Column(db.Integer, primary_key = True)
    plate = db.Column(db.String(6))
    model = db.Column(db.Integer())
    seats_num = db.Column(db.Integer())

    def __init__(self, plate, model, seats_num):
        self.plate = plate
        self.model = model
        self.seats_num = seats_num

with app.app_context():
    db.create_all()

class VehicleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'plate', 'model', 'seats_num')