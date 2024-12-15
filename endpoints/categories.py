from flask import Blueprint, request, jsonify
from utils.decorators import validate_token
from utils.repository_factory import get_repository
from utils.error_handler import ErrorHandler

categories_bp = Blueprint('categories', __name__)
category_repo = get_repository('categories')

@categories_bp.route('/categories', methods=['GET'])
@validate_token
def get_categories():
    try:
        categories = category_repo.get_all()
        return jsonify(categories), 200
    except Exception as e:
        return ErrorHandler.generate_error(str(e), 500)

@categories_bp.route('/categories', methods=['POST'])
@validate_token
def create_category():
    try:
        data = request.json
        category_name = data.get('name')
        if not category_name:
            return ErrorHandler.generate_error("Category name is required", 400)
        category_repo.add({'name': category_name})
        return jsonify({'message': 'Category created successfully'}), 201
    except Exception as e:
        return ErrorHandler.generate_error(str(e), 500)

@categories_bp.route('/categories/<int:category_id>', methods=['DELETE'])
@validate_token
def delete_category(category_id):
    try:
        if category_repo.delete(category_id):
            return jsonify({'message': 'Category deleted successfully'}), 200
        return ErrorHandler.generate_error("Category not found", 404)
    except Exception as e:
        return ErrorHandler.generate_error(str(e), 500)
