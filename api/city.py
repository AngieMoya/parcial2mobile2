from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.city import City, CitySchema

route_cities = Blueprint("route_cities", __name__)

city_schema = CitySchema()
cities_schema = CitySchema(many=True)

@route_cities.route('/cities', methods=['GET'])
def city():
    resultall = City.query.all()
    result_city = cities_schema.dump(resultall)
    return jsonify(result_city)

@route_cities.route('/savecity', methods=['POST'])
def save():
    name = request.json['name']
    department = request.json['department']
    new_city = City(name, department)
    db.session.add(new_city)
    db.session.commit()
    return jsonify(city_schema.dump(new_city))


@route_cities.route('/updatecity', methods=['PUT'])
def Update():
    id = request.json['id']
    name = request.json['name']
    department = request.json['department']
    city = City.query.get(id)
    if city:
        print(city)
        city.name = name
        city.department = department
        db.session.commit()
        return jsonify(city_schema.dump(city))
    else:
        return "Error"

@route_cities.route('/deletecity/<id>', methods=['DELETE'])
def delete(id):
    city = City.query.get(id)
    db.session.delete(city)
    db.session.commit()
    return jsonify(city_schema.dump(city))