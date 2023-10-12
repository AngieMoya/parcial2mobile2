from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.stop import Stop, StopSchema

route_stop = Blueprint("route_stops", __name__)

stop_schema = StopSchema()
stops_schema = StopSchema(many=True)

@route_stops.route('/stops', methods=['GET'])
def stop():
    resultall = Stop.query.all()
    result_stop = stops_schema.dump(resultall)
    return jsonify(result_stop)

@route_stops.route('/savestop', methods=['POST'])
def save():
    route = request.json['route']
    address_destiny = request.json['address_destiny']
    address_origin = request.json['address_origin']
    new_stop = Stop(route, address_destiny, address_origin)
    db.session.add(new_stop)
    db.session.commit()
    return jsonify(new_stop)

@route_stops.route('/updatestop', methods=['PUT'])
def Update():
    id = request.json['id']
    route = request.json['route']
    address_destiny = request.json['address_destiny']
    address_origin = request.json['address_origin']
    stop = Stop.query.get(id)
    if stop :
        print(stop)
        stop.route = route
        stop.address_destiny = address_destiny
        stop.address_origin = address_origin
        db.session.commit()
        return " Datos actualizados"
    else:
        return "Error"

@route_stops.route('/deletestop', methods=['DELETE'])
def delete(id):
    stop = Stop.query.get(id)
    db.session.delete(stop)
    db.session.commit()
    return jsonify(stop_schema.dump(stop))