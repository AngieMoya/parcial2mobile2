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
    request = request.json['request']
    state = request.json['state']
    payment_method = request.json['payment_method']
    new_payment = City(traveler, request, state, payment_method)
    db.session.add(new_payment)
    db.session.commit()
    return jsonify(payments_schema.dump(new_payment))

@route_payments.route('/updatepayment', methods=['PUT'])
def update():
    id = request.json['id']
    traveler = request.json['traveler']
    request = request.json['request']
    state = request.json['state']
    payment_method = request.json['payment_method']
    payment = Payment.query.get(id)
    if payment:
        payment.traveler = traveler
        payment.request = request
        payment.state = state
        payment.payment_method = payment_method
        db.session.commit()
        return jsonify(payments_schema.dump(payment))
    else:
        return "Error"

@route_payments.route('/deletepayment/<id>', methods=['DELETE'])
def delete(id):
    payment = Payment.query.get(id)
    db.session.delete(payment)
    db.session.commit()
    return jsonify(payments_schema.dump(payment))
