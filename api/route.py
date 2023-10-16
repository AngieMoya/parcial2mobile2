from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.route import Route, RouteSchema

route_routes = Blueprint("route_routes", __name__)

route_schema = RouteSchema()
routes_schema = RouteSchema(many=True)

@route_routes.route('/routes', methods=['GET'])
def route():
    resultall = Route.query.all()
    result_route = routes_schema.dump(resultall)
    return jsonify(result_route)

@route_routes.route('/saveroute', methods=['POST'])
def save():
    origin = request.json['origin']
    destination = request.json['destination']
    distance = request.json['distance']

    new_route = Route(origin, destination, distance)
    db.session.add(new_route)
    db.session.commit()
    return jsonify(route_schema.dump(new_route))

@route_routes.route('/updateroute', methods=['PUT'])
def Update():
    id = request.json['id']
    origin = request.json['origin']
    destination = request.json['destination']
    distance = request.json['distance']

    route = Route.query.get(id)
    if route:
        print(route)
        route.origin = origin
        route.destination = destination
        route.distance = distance

        db.session.commit()
        return jsonify(route_schema.dump(route))
    else:
        return "Error"

@route_routes.route('/deleteroute/<id>', methods=['DELETE'])
def delete(id):
    route = Route.query.get(id)
    db.session.delete(route)
    db.session.commit()
    return jsonify(route_schema.dump(route))
