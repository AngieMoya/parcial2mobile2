from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.payment import Payment, PaymentSchema

route_payments = Blueprint("route_payments", __name__)

payment_schema = PaymentSchema()
payments_schema = PaymentSchema(many=True)

@route_payments.route('/payments', methods=['GET'])
def payment():
    result_all = Payment.query.all()
    result_payments = payments_schema.dump(result_all)
    return jsonify(result_payments)

@route_payments.route('/savepayment', methods=['POST'])
def save():
    traveler = request.json['traveler']
    petition = request.json['request']
    state = request.json['state']
    payment_method = request.json['payment_method']
    limit_date = request.json['limit_date']
    payment_date = request.json['payment_date']

    new_payment = Payment(traveler, petition, state, payment_method, limit_date, payment_date)
    db.session.add(new_payment)
    db.session.commit()
    return jsonify(payment_schema.dump(new_payment))

@route_payments.route('/updatepayment', methods=['PUT'])
def update():
    id = request.json['id']
    traveler = request.json['traveler']
    petition = request.json['request']
    state = request.json['state']
    payment_method = request.json['payment_method']
    limit_date = request.json['limit_date']
    payment_date = request.json['payment_date']

    payment = Payment.query.get(id)
    if payment:
        payment.traveler = traveler
        payment.request = petition
        payment.state = state
        payment.payment_method = payment_method
        payment.limit_date = limit_date
        payment.payment_date = payment_date
        
        db.session.commit()
        return jsonify(payment_schema.dump(payment))
    else:
        return "Error"

@route_payments.route('/deletepayment/<id>', methods=['DELETE'])
def delete(id):
    payment = Payment.query.get(id)
    db.session.delete(payment)
    db.session.commit()
    return jsonify(payment_schema.dump(payment))
