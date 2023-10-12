from config.db import  db, ma, app

class Traveler(db.Model):
    __tablename__ = "tbltraveler"

    id = db.Column(db.Integer, primary_key =True)
    doc_type = db.Column(db.Integer(12))
    name = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    age = db.Column(db.Integer(2))
    email = db.Column(db.String(50))
    phone_number = db.Column(db.Integer(10))
    address = db.Column(db.String(50))

    def __init__(self, doc_type, name, lastname, age, email, phone_number, address) :
       self.doc_type = doc_type
       self.name = name
       self.lastname = lastname
       self.age = age
       self.email = email
       self.phone_number = phone_number
       self.address = address

with app.app_context():
    db.create_all()

class TravelerSchema(ma.Schema):
    class Meta:
        fields = ('id','doc_type','name','lastname','age','email','phone_number','address')
