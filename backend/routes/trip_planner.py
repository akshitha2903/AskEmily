from flask import Blueprint, jsonify, request
from services.trip_planning_service import plan_trip

trip_planner_bp = Blueprint('trip_planner', __name__)

@trip_planner_bp.route('/plan_trip', methods=['POST'])
def plan_trip_route():
    data = request.get_json()
    trip_details = plan_trip(data)
    return jsonify(trip_details), 200
