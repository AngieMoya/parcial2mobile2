from config.db import  db, ma, app

class Driver(db.Model):
    __tablename__ = "drivers"

    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    license = db.Column(db.String(50))
    status = db.Column(db.Integer)

    def __init__(self, name, lastname, license, status):
        self.name = name
        self.lastname = lastname
        self.license = license
        self.status = status

with app.app_context():
    db.create_all()

class DriverSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'lastname', 'license', 'status')
