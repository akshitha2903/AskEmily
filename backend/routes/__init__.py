from flask import Blueprint

# Creating a blueprint for the routes
bp = Blueprint('routes', __name__)

# Import all routes to ensure they are registered
from .trip_planner import trip_planner_bp
from .rv_technicians import rv_technician_bp
