from config.db import  db, ma, app

class DrivingDetail(db.Model):
    __tablename__ = "driving_details"

    id = db.Column(db.Integer, primary_key =True)
    vehicle = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    driver = db.Column(db.Integer, db.ForeignKey('drivers.id'))
    date_of_use = db.Column(db.DateTime)

    def __init__(self, vehicle, driver, date_of_use):
        self.vehicle = vehicle
        self.driver = driver
        self.date_of_use = date_of_use

with app.app_context():
    db.create_all()

class DrivingDetailSchema(ma.Schema):
    class Meta:
        fields = ('id', 'vehicle', 'driver', 'date_of_use')
        