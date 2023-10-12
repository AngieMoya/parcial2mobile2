from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.driver import Driver, DriverSchema

route_drivers = Blueprint("route_driver", __name__)

driver_schema = DriverSchema()
drivers_schema = DriverSchema(many=True)

@route_drivers.route('/drivers', methods=['GET'])
def driver():
    resultall = Driver.query.all()
    result_driver = drivers_schema.dump(resultall)
    return jsonify(result_driver)

@route_drivers.route('/savedriver', methods=['POST'])
def save():
    name = request.json['name']
    lastname = request.json['lastname']
    license = request.json['license']
    new_driver = Driver(name, lastname, license)
    db.session.add(new_driver)
    db.session.commit()
    return new_driver

@route_drivers.route('/updatedriver', methods=['PUT'])
def Update():
    id = request.json['id']
    name = request.json['name']
    lastname = request.json['lastname']
    license = request.json['license']
    driver = Driver.query.get(id)
    if driver:
        print(driver)
        driver.name = name
        driver.lastname = lastname
        driver.license = license
        db.session.commit()
        return "Datos actualizados"
    else:
        return "Error"

@route_drivers.route('/deletedriver/<id>', methods=['DELETE'])
def delete(id):
    driver = Driver.query.get(id)
    db.session.delete(driver)
    db.session.commit()
    return jsonify(driver_schema.dump(driver))