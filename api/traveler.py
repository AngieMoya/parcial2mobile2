from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.traveler import Traveler, TravelerSchema

route_travelers = Blueprint("route_traveler", __name__)

traveler_schema = TravelerSchema()
travelers_schema = TravelerSchema(many=True)

@route_travelers.route('/travelers', methods=['GET'])
def traveler():
    resultall = Traveler.query.all()
    result_traveler = travelers_schema.dump(resultall)
    return jsonify(result_traveler)

@route_travelers.route('/savetraveler', methods=['POST'])
def save():
    doc_type = request.json['document_type']
    name = request.json['name']
    lastname = request.json['lastname']
    age = request.json['age']
    email = request.json['email']
    phone_number = request.json['phone_number']
    address = request.json['address']
    new_traveler = Traveler(doc_type, name, lastname, age, email, phone_number,address)
    db.session.add(new_traveler)
    db.session.commit()
    return jsonify(new_traveler)

@route_travelers.route('/updatetraveler', methods=['PUT'])
def Update():
    id = request.json['id']
    doc_type = request.json['document_type']
    name = request.json['name']
    lastname = request.json['lastname']
    age = request.json['age']
    email = request.json['email']
    phone_number = request.json['phone_number']
    address = request.json['address']
    traveler = Traveler.query.get(id)
    if traveler :
        print(traveler)
        traveler.doc_type = doc_type
        traveler.name = name
        traveler.lastname = lastname
        traveler.age = age
        traveler.email = email
        traveler.phone_number = phone_number
        traveler.address = address
        db.session.commit()
        return "Datos actualizados"
    else:
        return "Error"

@route_travelers.route('/deletetraveler/<id>', methods=['DELETE'])
def delete(id):
    traveler = Traveler.query.get(id)
    db.session.delete(traveler)
    db.session.commit()
    return jsonify(traveler_schema.dump(traveler))
