from flask import Flask, jsonify,json
from config.db import  db, ma, app

#importar las api's
from api.city import City, route_cities
from api.traveler import Traveler, route_travelers
from api.driver import Driver, route_drivers
from api.vehicle import Vehicle, route_vehicles
from api.driving_detail import DrivingDetail, route_driving_details
from api.route import Route, route_routes
from api.trip import Trip, route_trips
from api.stop import Stop, route_stops

app.register_blueprint(route_cities, url_prefix = '/api')
app.register_blueprint(route_travelers, url_prefix = '/api')
app.register_blueprint(route_drivers, url_prefix = '/api')
app.register_blueprint(route_vehicles, url_prefix = '/api')
app.register_blueprint(route_driving_details, url_prefix = '/api')
app.register_blueprint(route_routes, url_prefix = '/api')
app.register_blueprint(route_trips, url_prefix = '/api')
app.register_blueprint(route_stops, url_prefix = '/api')

@app.route('/api')
def index():
    return "Hola Mundo"

# @app.route('/dostablas', methods=['GET'])
# def dostabla():
#     datos = {}
#     resultado = db.session.query(Cliente, Reserva). \
#         select_from(Cliente).join(Reserva).all()
#     i=0
#     for clientes, reservas in resultado:
#         i+=1
#         datos[i]={
#             'cliente':clientes.nombre,
#             'reserva': reservas.id
#         }
#     return datos

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')