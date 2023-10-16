from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.request import Request, RequestSchema

route_requests = Blueprint("route_requests", __name__)

request_schema = RequestSchema()
requests_schema = RequestSchema(many=True)

@route_requests.route('/requests', methods=['GET'])
def petition():
    result_all = Request.query.all()
    result_requests = requests_schema.dump(result_all)
    return jsonify(result_requests)

@route_requests.route('/saverequest', methods=['POST'])
def save():
    stop = request.json['stop']
    traveler = request.json['traveler']
    origin_city = request.json['origin_city']
    destiny_city = request.json['destiny_city']
    trip = request.json['trip']
    seats = request.json['seats']
    preferences = request.json['preferences']
    new_request = Request(traveler, stop, origin_city, destiny_city, trip, seats, preferences)
    db.session.add(new_request)
    db.session.commit()
    return jsonify(request_schema.dump(new_request))

@route_requests.route('/updaterequest', methods=['PUT'])
def update():
    id = request.json['id']
    traveler = request.json['traveler']
    stop = request.json['stop']
    origin_city = request.json['origin_city']
    destiny_city = request.json['destiny_city']
    trip = request.json['trip']
    seats = request.json['seats']
    preferences = request.json['preferences']

    petition = Request.query.get(id)
    if petition:
        petition.traveler = traveler
        petition.stop = stop
        petition.origin_city = origin_city
        petition.destiny_city = destiny_city
        petition.trip = trip
        petition.seats = seats
        petition.preferences = preferences
        db.session.commit()
        return jsonify(request_schema.dump(petition))
    else:
        return "Error"

@route_requests.route('/deleterequest/<id>', methods=['DELETE'])
def delete(id):
    request = Request.query.get(id)
    db.session.delete(request)
    db.session.commit()
    return jsonify(request_schema.dump(request))
