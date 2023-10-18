from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.trip import Trip, TripSchema
from models.vehicle import Vehicle, VehicleSchema

route_trips = Blueprint("route_trips", __name__)

trip_schema = TripSchema()
trips_schema = TripSchema(many=True)
vehicles_schema = VehicleSchema(many=True)

@route_trips.route('/trips', methods=['GET'])
def trip():
    result_all = Trip.query.all()
    result_trips = trips_schema.dump(result_all)
    return jsonify(result_trips)

@route_trips.route('/savetrip', methods=['POST'])
def save():
    vehicles = db.session.query(Vehicle).filter(Vehicle.status == 1)
    if len(vehicles_schema.dump(vehicles)) == 0:
        raise Exception('No vehicle found')
    else:
        to_assign = vehicles_schema.dump(vehicles)[0]["id"]
        vehicle = to_assign
        to_update = Vehicle.query.get(to_assign)
        to_update.status = 0

        route = request.json['route']
        start_time = request.json['start_time']
        ending_time = request.json['ending_time']
    
        new_trip = Trip(vehicle, route, start_time, ending_time)
        print (f"vehicle to assing: {new_trip}")

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
