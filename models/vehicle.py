from config.db import  db, ma, app

class Vehicle(db.Model):
    __tablename__ = "vehicles"

    id = db.Column(db.Integer, primary_key = True)
    driver = db.Column(db.Integer, ForeignKey('drivers'))
    model = db.Column(db.Integer(4))
    seats_num = db.Column(db.Integer(2))

    def __init__(self, driver, model, seats_num):
        self.driver = driver
        self.model = model
        self.seats_num = seats_num

with app.app_context():
    db.create_all()

class VehicleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'driver', 'model', 'seats_num')