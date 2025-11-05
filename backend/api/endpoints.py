from flask import Blueprint, request, jsonify
from backend.ai.inference.predictor import Predictor

api = Blueprint('api', __name__)
predictor = Predictor()

@api.route('/optimize/pfc', methods=['POST'])
def optimize_pfc():
    data = request.json
    if not data or 'parameters' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    parameters = data['parameters']
    optimization_result = predictor.optimize_pfc(parameters)
    
    return jsonify(optimization_result), 200

@api.route('/optimize/buck', methods=['POST'])
def optimize_buck():
    data = request.json
    if not data or 'parameters' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    parameters = data['parameters']
    optimization_result = predictor.optimize_buck(parameters)
    
    return jsonify(optimization_result), 200

@api.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200