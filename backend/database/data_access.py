from pymongo import MongoClient

# Initialize MongoDB client
client = MongoClient('mongodb://localhost:27017/')  # Adjust as needed
db = client['AskEmily']  # Your database name

def get_technicians_from_db():
    return list(db.technicians.find({}))

def save_technician_to_db(technician):
    # Make sure this function returns the result of the insert operation
    return db.technicians.insert_one(technician)  # This should return an InsertOneResult object
