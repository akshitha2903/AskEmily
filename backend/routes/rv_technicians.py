from flask import Blueprint, jsonify, request
from services.technician_service import find_technician, add_technician_to_db

rv_technician_bp = Blueprint('rv_technician', __name__)

@rv_technician_bp.route('/technicians', methods=['GET'])
def get_technicians():
    technicians = find_technician()  # This function retrieves technicians from the database
    return jsonify(technicians), 200

from flask import Blueprint, request, jsonify, current_app

@rv_technician_bp.route('/technicians', methods=['POST'])

def add_technician():
    data = request.json
    current_app.logger.debug(f'Received data: {data}')  # Log incoming data

    # Validate incoming data
    if not data or 'name' not in data or 'specialty' not in data:
        current_app.logger.error("Missing required fields: name and specialty.")
        return jsonify({"error": "Missing required fields: name and specialty."}), 400
    
    technician = {
        "name": data["name"],
        "specialty": data["specialty"]
    }
    
    # Attempt to add technician to DB
    try:
        technician_id = add_technician_to_db(technician)  # Call service function
        current_app.logger.info("Technician added: %s", technician)
    except Exception as e:
        current_app.logger.error("Error adding technician: %s", str(e))  # Log the error
        return jsonify({"error": f"An error occurred while adding the technician: {str(e)}"}), 500

    # Convert ObjectId to string for the response
    return jsonify({
        "message": "Technician added successfully!", 
        "data": {
            "id": str(technician_id),
            "name": technician["name"],
            "specialty": technician["specialty"]
        }
    }), 201
