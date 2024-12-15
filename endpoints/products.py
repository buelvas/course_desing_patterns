from flask import Blueprint, request, jsonify
from utils.decorators import validate_token
from utils.repository_factory import get_repository
from utils.error_handler import ErrorHandler

products_bp = Blueprint('products', __name__)
product_repo = get_repository('products')

@products_bp.route('/products', methods=['GET'])
@validate_token
def get_products():
    try:
        category = request.args.get('category')
        if category:
            products = product_repo.get_products_by_category(category)
        else:
            products = product_repo.get_all()
        return jsonify(products), 200
    except Exception as e:
        return ErrorHandler.generate_error(str(e), 500)

@products_bp.route('/products/<int:product_id>', methods=['GET'])
@validate_token
def get_product(product_id):
    try:
        product = product_repo.get_by_id(product_id)
        if product:
            return jsonify(product), 200
        return ErrorHandler.generate_error("Product not found", 404)
    except Exception as e:
        return ErrorHandler.generate_error(str(e), 500)

@products_bp.route('/products', methods=['POST'])
@validate_token
def create_product():
    try:
        data = request.json
        product_repo.add(data)
        return jsonify({'message': 'Product created successfully'}), 201
    except Exception as e:
        return ErrorHandler.generate_error(str(e), 500)



