from config.db import  db, ma, app

class Traveler(db.Model):
    __tablename__ = "travelers"

    id = db.Column(db.Integer, primary_key =True)
    doc_type = db.Column(db.Integer())
    name = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    age = db.Column(db.Integer())
    email = db.Column(db.String(50))
    phone_number = db.Column(db.Integer())
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
