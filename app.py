from flask import Flask
from endpoints.auth import auth_bp
from endpoints.products import products_bp
from endpoints.categories import categories_bp
from endpoints.favorites import favorites_bp

app = Flask(__name__)
app.register_blueprint(auth_bp)
app.register_blueprint(products_bp)
app.register_blueprint(categories_bp)
app.register_blueprint(favorites_bp)

if __name__ == '__main__':
    app.run(debug=True)


