from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from models.models import Restaurante
from database import db
from schema.schemas import restaurantes_schema

from app.models.models import Restaurante

blueprint = Blueprint('app', __name__)

#Home route
@blueprint.route('/', methods=['GET'])
def inicio():
    return jsonify(respuesta='Rest API con Python, Flask y MySQL')

#Protected routes (CRUD)

#Create Restaurante
@blueprint.route('/api/restaurantes', methods=['POST'])
@jwt_required()
def create_restaurante():
    try:
        id = request.json['id']
        rating = request.json['rating']
        name = request.json['name']
        site = request.json['site']
        email = request.json['email']
        phone = request.json['phone']
        street = request.json['street']
        city = request.json['city']
        state = request.json['state']
        lat = request.json['lat']
        lng = request.json['lng']

        new_restaurante = Restaurante(id, rating, name, site, email, phone, street, city, state, lat, lng)

        db.session.add(new_restaurante)
        db.session.commit()

        return jsonify(respuesta='Restaurante Almacenado Exitosamente'), 201
    except Exception:
        return jsonify(respuesta='Error en Petición'),500

#Read Restaurante
@blueprint.route('/api/restaurantes', methods=['GET'])
@jwt_required()
def read_restaurante():
    try:
        restaurantes = Restaurante.query.all()
        respuesta = restaurantes_schema.dump(restaurantes)
        return jsonify(respuesta), 200
    except Exception:
        return jsonify(respuesta='Error en Petición'),500

#Read by Id Restaurante
@blueprint.route('/api/restaurantes/<String:id>', methods=['GET'])
@jwt_required()
def read_restaurante_by_id(id):
    try:
        restaurante = Restaurante.query.get(id)
        respuesta = restaurantes_schema.dump(restaurante)
        return jsonify(respuesta), 200
    except Exception:
        return jsonify(respuesta='Error en Petición'),500

#Update Restaurante
@blueprint.route('/api/restaurantes/<String:id>', methods=['PUT'])
@jwt_required()
def update_restaurante(id):
    try:
        restaurante = Restaurante.query.get(id)
        if not restaurante:
            return jsonify(respuesta='Restaurante No Encontrado'), 404
        
        restaurante.id = request.json['id']
        restaurante.rating = request.json['rating']
        restaurante.name = request.json['name']
        restaurante.site = request.json['site']
        restaurante.email = request.json['email']
        restaurante.phone = request.json['phone']
        restaurante.street = request.json['street']
        restaurante.city = request.json['city']
        restaurante.state = request.json['state']
        restaurante.lat = request.json['lat']
        restaurante.lng = request.json['lng']

        db.session.commit()

        return jsonify(respuesta='Restaurante Actualizado Exitosamente'), 200
    except Exception:
        return jsonify(respuesta='Error en Petición'),500

#Delete by Id Restaurante
@blueprint.route('/api/restaurantes/<String:id>', methods=['DELETE'])
@jwt_required()
def delete_restaurante_by_id(id):
    try:
        restaurante = Restaurante.query.get(id)
        if not restaurante:
            return jsonify(respuesta='Restaurante No Encontrado'), 404
        
        db.session.delete(restaurante)
        db.session.commit()
        
        return jsonify(respuesta='Restaurante Eliminado Exitosamente'), 200
    except Exception:
        return jsonify(respuesta='Error en Petición'),500