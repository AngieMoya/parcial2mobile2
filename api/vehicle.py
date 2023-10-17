from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.vehicle import Vehicle, VehicleSchema

route_vehicles = Blueprint("route_vehicle", __name__)

vehicle_schema = VehicleSchema()
vehicles_schema = VehicleSchema(many=True)

@route_vehicles.route('/vehicles', methods=['GET'])
def vehicle():
    resultall = Vehicle.query.all()
    result_vehicles = vehicles_schema.dump(resultall)
    return jsonify(result_vehicles)

@route_vehicles.route('/savevehicle', methods=['POST'])
def save():
    plate = request.json['plate']
    model = request.json['model']
    seats_num = request.json['seats_num']
    status = request.json['status']

    new_vehicle = Vehicle(plate, model, seats_num, status)
    db.session.add(new_vehicle)
    db.session.commit()
    return jsonify(vehicle_schema.dump(new_vehicle))



@route_vehicles.route('/updatevehicle', methods=['PUT'])
def Update():
    id = request.json['id']
    plate = request.json['plate']
    model = request.json['model']
    seats_num = request.json['seats_num']
    status = request.json['status']

    vehicle = Vehicle.query.get(id)
    if vehicle:
        print(vehicle)
        vehicle.plate = plate
        vehicle.model = model
        vehicle.seats_num = seats_num
        vehicle.status = status
        
        db.session.commit()
        return jsonify(vehicle_schema.dump(vehicle))
    else:
        return "Error"

@route_vehicles.route('/deletevehicle/<id>', methods=['DELETE'])
def delete(id):
    vehicle = Vehicle.query.get(id)
    db.session.delete(vehicle)
    db.session.commit()
    return jsonify(vehicle_schema.dump(vehicle))