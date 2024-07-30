from flask import Blueprint, current_app, request, jsonify

inmobiliary_bp = Blueprint('inmobiliary', __name__)

inmobiliary_model = current_app.inmobiliary_model

@inmobiliary_bp.route('/create')
def create():
    data = request.get_json()
    if not data:
        return jsonify(message="Invalid JSON"), 400

    if inmobiliary_model.create_inmobiliary(**data):
        return jsonify(message="Inmobiliary created successfully"), 201
    else:
        return jsonify(message="Inmobiliary corporative name alredy exists"), 409

@inmobiliary_bp.route('/update/<inmobiliary_id>', methods=['PUT'])
def update_inmobiliary(inmobiliary_id):
    data = request.get_json()
    if not data:
        return jsonify(message="Invalid JSON"), 400

    if inmobiliary_model.update_inmobiliary(inmobiliary_id, **data):
        return jsonify(message="Inmobiliary updated successfully"), 200
    else:
        return jsonify(message="Error updating Inmobiliary"), 500

@inmobiliary_bp.route('/delete/<inmobiliary_id>')
def delete_inmobiliary(inmobiliary_id):
    if inmobiliary_model.delete_inmobiliary(inmobiliary_id):
        return jsonify(message="Inmobiliary deleted successfully"), 200
    else:
        return jsonify(message="Inmobiliary not found"), 404

@inmobiliary_bp.route('/<inmobiliary_id>')
def get_inmobiliary(inmobiliary_id):
    inmobiliary = inmobiliary_model.find_inmobiliary_by_id(inmobiliary_id)
    if inmobiliary:
        return jsonify(inmobiliary), 200
    else:
        return jsonify(message="Inmobiliary not found"), 404

@inmobiliary_bp.route('/inmobiliarias')
def get_all_inmobiliaries():
    all_inmobiliaries = inmobiliary_model.get_all_inmobiliaries()
    return jsonify(inmobiliaries=all_inmobiliaries), 200
