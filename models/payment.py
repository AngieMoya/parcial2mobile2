from config.db import  db, ma, app

class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key =True)
    traveler = db.Column(db.Integer, db.ForeignKey('travelers.id'))
    request = db.Column(db.Integer, db.ForeignKey('requests.id'))
    state = db.Column(db.String(20))
    payment_method = db.Column(db.String(50))
    limit_date = db.Column(db.DateTime)
    payment_date = db.Column(db.DateTime)

    def __init__(self, traveler, request, state, payment_method, limit_date, payment_date):
        self.traveler = traveler
        self.request = request
        self.state = state
        self.payment_method = payment_method
        self.limit_date = limit_date
        self.payment_date = payment_date

with app.app_context():
    db.create_all()

class PaymentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'traveler', 'request', 'state', 'payment_method', 'limit_date', 'payment_date')