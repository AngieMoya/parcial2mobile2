from config.db import  db, ma, app

class DrivingDetail(db.Model):
    __tablename__ = "driving_details"

    id = db.Column(db.Integer, primary_key =True)
    vehicle = db.Column(db.Integer, ForeignKey('vehicles'))
    driver = db.Column(db.Integer, ForeignKey('drivers'))

    def __init__(self, vehicle, driver):
        self.vehicle = vehicle
        self.driver = driver

with app.app_context():
    db.create_all()

class DrivingDetailSchema(ma.Schema):
    class Meta:
        fields = ('id', 'vehicle', 'driver')
        