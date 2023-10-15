from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.request import Request, RequestSchema

route_requests = Blueprint("route_requests", __name__)

request_schema = RequestSchema()
requests_schema = RequestSchema(many=True)

@route_requests.route('/requests', methods=['GET'])
def request():
    result_all = request.query.all()
    result_requests = requests_schema.dump(result_all)
    return jsonify(result_requests)

@route_requests.route('/saverequest', methods=['POST'])
def save():
    traveler = request.json['traveler']
    stop = request.json['stop']
    origin_city = request.json['origin_city']
    destiny_city = request.json['destiny_city']
    trip = request.json['trip']
    seats = request.json['seats']
    preferences = request.json['preferences']

    new_request = City(traveler, stop, origin_city, destiny_city, trip, seats, preferences)
    db.session.add(new_request)
    db.session.commit()
    return jsonify(requests_schema.dump(new_request))

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

    request = Request.query.get(id)
    if request:
        request.traveler = traveler
        request.stop = stop
        request.origin_city = origin_city
        request.destiny_city = destiny_city
        request.trip = trip
        request.seats = seats
        request.preferences = preferences
        db.session.commit()
        return jsonify(requests_schema.dump(request))
    else:
        return "Error"

@route_requests.route('/deleterequest/<id>', methods=['DELETE'])
def delete(id):
    request = Request.query.get(id)
    db.session.delete(request)
    db.session.commit()
    return jsonify(requests_schema.dump(request))
