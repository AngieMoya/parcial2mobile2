from config.db import  db, ma, app

class City(db.Model):
    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(50))
    department = db.Column(db.String(50))

    def __init__(self, name, department):
        self.name = name
        self.department = department

with app.app_context():
    db.create_all()

class CitySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'department')