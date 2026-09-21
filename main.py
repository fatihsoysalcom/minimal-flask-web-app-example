# main.py
from flask import Flask, jsonify

# Initialize the Flask application
# This is the entry point for our web server, similar to how Django or FastAPI would start.
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    """
    This route demonstrates a basic HTML response for the root URL.
    It's the simplest form of a web page served by the framework.
    """
    return "<h1>Merhaba Dünya!</h1><p>Bu, Flask ile oluşturulmuş basit bir web uygulamasıdır.</p>"

# Define a route that returns JSON data
@app.route('/api/hello')
def api_hello():
    """
    This route demonstrates returning JSON data, which is common for API endpoints.
    FastAPI excels at this, but Flask and Django can also easily serve JSON.
    """
    return jsonify(message="Merhaba FastAPI ve Django!", framework="Flask", year=2026)

# Define a route with a path parameter
@app.route('/greet/<name>')
def greet_name(name):
    """
    This route demonstrates using path parameters to personalize responses.
    All three frameworks (Django, Flask, FastAPI) support dynamic routing like this.
    """
    return f"<h1>Merhaba, {name.capitalize()}!</h1><p>Flask ile kişiselleştirilmiş bir karşılama.</p>"

# Run the application
if __name__ == '__main__':
    # Flask applications typically run on port 5000 by default.
    # debug=True allows for automatic reloading on code changes and provides a debugger.
    # This 'run' command starts the development server.
    app.run(debug=True)