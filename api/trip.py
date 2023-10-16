from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.trip import Trip, TripSchema

route_trips = Blueprint("route_trips", __name__)

trip_schema = TripSchema()
trips_schema = TripSchema(many=True)

@route_trips.route('/trips', methods=['GET'])
def trip():
    result_all = Trip.query.all()
    result_trips = trips_schema.dump(result_all)
    return jsonify(result_trips)

@route_trips.route('/savetrip', methods=['POST'])
def save():
    vehicle = request.json['vehicle']
    route = request.json['route']
    start_time = request.json['start_time']
    ending_time = request.json['ending_time']

    new_trip = Trip(vehicle, route, start_time, ending_time)
    db.session.add(new_trip)
    db.session.commit()
    return jsonify(trip_schema.dump(new_trip))

@route_trips.route('/updatetrip', methods=['PUT'])
def update():
    id = request.json['id']
    vehicle = request.json['vehicle']
    route = request.json['route']
    start_time = request.json['start_time']
    ending_time = request.json['ending_time']
    trip = Trip.query.get(id)
    if trip:
        trip.vehicle = vehicle
        trip.route = route
        trip.start_time = start_time
        trip.ending_time = ending_time
        db.session.commit()
        return jsonify(trip_schema.dump(trip))
    else:
        return "Error"

@route_trips.route('/deletetrip/<id>', methods=['DELETE'])
def delete(id):
    trip = Trip.query.get(id)
    db.session.delete(trip)
    db.session.commit()
    return jsonify(trip_schema.dump(trip))
