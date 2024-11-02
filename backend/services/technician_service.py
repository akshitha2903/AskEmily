from database.data_access import get_technicians_from_db, save_technician_to_db
from bson import ObjectId  # Import ObjectId from bson

def find_technician():
    # Retrieve technicians from the database
    technicians = get_technicians_from_db()
    
    # Convert ObjectId to string
    for technician in technicians:
        technician['_id'] = str(technician['_id'])  # Convert ObjectId to string
        
    return technicians

def add_technician_to_db(technician):
    # Save technician to the database
    result = save_technician_to_db(technician)  # Use the data access function to insert
    return result.inserted_id  # Return the ObjectId of the new technician
