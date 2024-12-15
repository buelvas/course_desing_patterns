from flask import jsonify

class ErrorHandler:
    @staticmethod
    def generate_error(message, code):
        response = {"error": message}
        return jsonify(response), code
