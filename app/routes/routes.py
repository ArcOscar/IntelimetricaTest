from flask import Blueprint, request, jsonify

blueprint = Blueprint('app', __name__)

#Home route
@blueprint.route('/', methods=['GET'])
def inicio():
    return "<h1>Flask API</h1>"