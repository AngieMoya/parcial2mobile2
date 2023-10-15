from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.driving_details import DrivingDetail, DrivingDetailSchema

route_driving_details = Blueprint("route_driving_details", __name__)

detail_schema = DrivingDetailSchema()
details_schema = DrivingDetailSchema(many=True)

@route_driving_details.route('/driving_details', methods=['GET'])
def driving_detail():
    result_all = DrivingDetail.query.all()
    result_details = details_schema.dump(result_all)
    return jsonify(result_details)

@route_driving_details.route('/savedetails', methods=['POST'])
def save():
    vehicle = request.json['vehicle']
    driver = request.json['driver']
    new_detail = City(vehicle, driver)
    db.session.add(new_detail)
    db.session.commit()
    return jsonify(details_schema.dump(new_detail))

@route_driving_details.route('/updatedetails', methods=['PUT'])
def update():
    id = request.json['id']
    vehicle = request.json['vehicle']
    driver = request.json['driver']
    detail = DrivingDetail.query.get(id)
    if detail:
        detail.vehicle = vehicle
        detail.detail = detail
        db.session.commit()
        return jsonify(details_schema.dump(detail))
    else:
        return "Error"

@route_driving_details.route('/deletedetails/<id>', methods=['DELETE'])
def delete(id):
    detail = DrivingDetail.query.get(id)
    db.session.delete(detail)
    db.session.commit()
    return jsonify(details_schema.dump(detail))
