from flask import Flask
from flask_pymongo import PyMongo
from routes.rv_technicians import rv_technician_bp
from flask import Flask,request, jsonify 
import requests 
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/AskEmily"  # Update this as needed
mongo = PyMongo(app)  # Set the Mongo instance

@app.route('/')
def home():
    return "Welcome to Ask Emily API!"

# Register blueprints here
def register_routes():
    from routes.trip_planner import trip_planner_bp
    from routes.rv_technicians import rv_technician_bp
    app.register_blueprint(trip_planner_bp)
    app.register_blueprint(rv_technician_bp)

register_routes()  # Call the function to register routes
# Replace with your actual Google Maps API key
GOOGLE_MAPS_API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'

@app.route('/route', methods=['POST'])
def get_route():
    data = request.json
    origin = data['origin']
    destination = data['destination']
    
    # Example parameters, you can customize as needed
    params = {
        'origin': origin,
        'destination': destination,
        'key': GOOGLE_MAPS_API_KEY
    }
    
    response = requests.get('https://maps.googleapis.com/maps/api/directions/json', params=params)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
