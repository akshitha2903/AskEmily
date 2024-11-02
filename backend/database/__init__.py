from pymongo import MongoClient

# Initialize MongoDB client
client = MongoClient('mongodb://localhost:27017/')  # Change to your MongoDB connection string
db = client['AskEmily']  # Replace with your database name
