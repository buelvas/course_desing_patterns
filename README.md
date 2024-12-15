# Description

The following is a simple implementation of a REST API with poor coding practices and no software design. Try to improve this code by applying everything you've learned about software design patterns, clean code, and SOLID principles.

# How to Run

1. **Download Python** from [Python Official Website](https://www.python.org/downloads/).

2. **Install Python** and set up the environment variable.

3. **Open Git Bash.** I recommend using Git Bash for the following steps.

4. **Clone this repository** or unzip the folder and go to the folder
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

5. **Create a virtual environment** using the following command:
   ```bash
   python -m venv venv
   ```

6. **Activate the virtual environment** with this command:
   ```bash
   source venv/bin/activate      # On Linux/macOS
   venv\Scripts\activate       # On Windows
   ```

7. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   **Dependencies in `requirements.txt` include:**
   ```plaintext
   Flask==2.2.3
   ```
   These are the required libraries to run the project.

8. **Run** the Flask app with this command:
   ```bash
   python app.py
   ```

9. **Test the API** using tools like Postman, Insomnia, or curl.
   Example:
   ```bash
   curl -X GET http://127.0.0.1:5000/products -H "Authorization: abcd12345"
   ```

# Endpoints

1. **Login**: Returns a static token for authentication.
    - **Method**: POST
    - **Path**: /auth

2. **Products**:

   - **Get Products**
     ```
     {
         "method": "GET",
         "path": "/products",
         "authToken": "required"
     }
     ```

   - **Get Product**
     ```
     {
         "method": "GET",
         "path": "/products/productId",
         "authToken": "required"
     }
     ```

   - **Get Products by Category**
     ```
     {
         "method": "GET",
         "path": "/products?category=categoryName",
         "authToken": "required"
     }
     ```

   - **Create Product**
     ```
     {
         "method": "POST",
         "path": "/products",
         "authToken": "required",
         "body": {
             "name": "nameProduct",
             "category": "categoryProduct",
             "price": 9
         }
     }
     ```

3. **Categories**

   - **Get Categories**
     ```
     {
         "method": "GET",
         "path": "/categories",
         "authToken": "required"
     }
     ```

   - **Create Category**
     ```
     {
         "method": "POST",
         "path": "/categories",
         "authToken": "required",
         "body": {
             "name": "nameCategory"
         }
     }
     ```

   - **Delete Category**
     ```
     {
         "method": "DELETE",
         "path": "/categories",
         "authToken": "required",
         "body": {
             "name": "nameCategory"
         }
     }
     ```

4. **Favorites**:

   - **Get Favorites**
     ```
     {
         "method": "GET",
         "path": "/favorites",
         "authToken": "required"
     }
     ```

   - **Add Favorite**
     ```
     {
         "method": "POST",
         "path": "/favorites",
         "authToken": "required",
         "body": {
             "productId": 123
         }
     }
     ```

   - **Delete Favorite**
     ```
     {
         "method": "DELETE",
         "path": "/favorites/favoriteId",
         "authToken": "required"
     }
     ```

# Project Structure

```plaintext
project/
|-- app.py
|-- db.json
|-- endpoints/
|   |-- products.py
|   |-- categories.py
|   |-- favorites.py
|   |-- auth.py
|-- utils/
|   |-- decorators.py
|   |-- error_handler.py
|   |-- repositories.py
|   |-- repository_factory.py
```

# Contribution

Contributions are welcome! Open an issue or submit a pull request. Please follow coding standards and document your changes.
