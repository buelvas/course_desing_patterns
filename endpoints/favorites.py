from flask import Blueprint, request, jsonify
from utils.decorators import validate_token
from utils.repository_factory import get_repository
from utils.error_handler import ErrorHandler

favorites_bp = Blueprint('favorites', __name__)
favorite_repo = get_repository('favorites')

@favorites_bp.route('/favorites', methods=['GET'])
@validate_token
def get_favorites():
    try:
        favorites = favorite_repo.get_all()
        return jsonify(favorites), 200
    except Exception as e:
        return ErrorHandler.generate_error(str(e), 500)

@favorites_bp.route('/favorites', methods=['POST'])
@validate_token
def add_favorite():
    try:
        data = request.json
        product_id = data.get('productId')
        if not product_id:
            return ErrorHandler.generate_error("Product ID is required", 400)
        favorite_repo.add({'productId': product_id})
        return jsonify({'message': 'Favorite added successfully'}), 201
    except Exception as e:
        return ErrorHandler.generate_error(str(e), 500)

@favorites_bp.route('/favorites/<int:favorite_id>', methods=['DELETE'])
@validate_token
def delete_favorite(favorite_id):
    try:
        if favorite_repo.delete(favorite_id):
            return jsonify({'message': 'Favorite deleted successfully'}), 200
        return ErrorHandler.generate_error("Favorite not found", 404)
    except Exception as e:
        return ErrorHandler.generate_error(str(e), 500)

