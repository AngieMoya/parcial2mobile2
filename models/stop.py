from config.db import  db, ma, app

class Stop(db.Model):
    __tablename__ = "tblstop"

    id = db.Column(db.Integer, primary_key =True)
    route = db.Column(db.Integer, db.ForeignKey('tblroute'))
    address_destiny = db.Column(db.String(50))
    address_origin = db.Column(db.String(50))

    def __init__(self, route, address_destiny, address_origin):
        self.route = route
        self.address_destiny = address_destiny
        self.address_origin = address_origin

with app.app_context():
    db.create_all()

class StopSchema(ma.Schema):
    class Meta:
        fields = ('id','route', 'address_destiny', 'address_origin')