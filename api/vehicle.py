from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.vehicle import Vehicle, VehicleSchema

route_vehicles = Blueprint("route_vehicle", __name__)

vehicle_schema = VehicleSchema()
vehicles_schema = VehicleSchema(many=True)

@route_vehicles.route('/vehicles', methods=['GET'])
def vehicle():
    resultall = Vehicle.query.all()
    result_vehicle = vehicles_schema.dump(resultall)
    return jsonify(result_vehicle)

@route_vehicles.route('/savevehicle', methods=['POST'])
def save():
    driver = request.json['doc_type']
    model = request.json['model']
    seats_num = request.json['seats_num']
    new_vehicle = Vehicle(driver, model, seats_num)
    db.session.add(new_vehicle)
    db.session.commit()
    return jsonify(new_traveler)


@route_vehicles.route('/updatevehicle', methods=['PUT'])
def Update():
    id = request.json['id']
    driver = request.json['driver']
    model = request.json['model']
    seats_num = request.json['seats_num']
    vehicle = Vehicle.query.get(id)
    if vehicle:
        print(vehicle)
        vehicle.driver = driver
        vehicle.model = model
        vehicle.seats_num = seats_num
        db.session.commit()
        return "Datos actualizados"
    else:
        return "Error"

@route_vehicles.route('/deletevehicle/<id>', methods=['DELETE'])
def delete(id):
    vehicle = Vehicle.query.get(id)
    db.session.delete(vehicle)
    db.session.commit()
    return jsonify(vehicle_schema.dump(vehicle))