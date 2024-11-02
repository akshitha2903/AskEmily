# Ask Emily - AI Trip Planner, Travel Advisor, GPS & RV Technician Finder

**Ask Emily** is an AI-powered trip planner and travel advisor application designed to assist users in planning their trips, finding RV technicians, and providing tailored recommendations. The system integrates Google Maps for route planning and utilizes a MongoDB database to manage RV technician information.

## Features

- **Route Planning**: Users can request directions between two locations using Google Maps API.
- **RV Technician Finder**: Users can retrieve a list of available RV technicians from a MongoDB database.

## Technologies Used

- **Backend**: Flask
- **Database**: MongoDB (via Flask-PyMongo)
- **API**: Google Maps Directions API
- **Testing**: Postman for API testing

## Setup Instructions

1. **Clone the Repository**:
   bash
   git clone https://github.com/yourusername/ask-emily.git
   cd ask-emily
   

2. **Install Dependencies**: Ensure you have Python installed, then install the required libraries:
   bash
   pip install Flask Flask-PyMongo requests
   

3. **Set Up MongoDB**: Ensure you have a local MongoDB instance running. You can download it from the [MongoDB Download Center](https://www.mongodb.com/try/download/community).

4. **Insert Sample Data (Run once)**:
   python
   from app import mongo
   technicians = [
       {"name": "John Doe", "location": "Los Angeles", "specialty": "Engine Repair"},
       {"name": "Jane Smith", "location": "San Francisco", "specialty": "Electrical"},
   ]
   mongo.db.technicians.insert_many(technicians)
   

5. **Run the Application**: Start the Flask server:
   bash
   python app.py
   

## API Endpoints

- **Home Endpoint**:
  - **GET /** 
  - **Response**: "Welcome to Ask Emily API!"

- **Route Planning**:
  - **POST /route**
  - **Request Body**:
    json
    {
        "origin": "San Francisco, CA",
        "destination": "Los Angeles, CA"
    }
    
  - **Response**: JSON with route details from Google Maps API.

- **RV Technicians**:
  - **GET /technicians**
  - **Response**: List of RV technicians with their details.

## Screenshots

- MongoDB Database  
  ![MongoDB Database](D:\Akshi\projects\AskEmily\backend\mongodb.png)

- Sample Data in MongoDB  
  ![Sample Data](D:\Akshi\projects\AskEmily\backend\postman.png)

## Future Improvements

- Integration of GPS functionality for real-time route tracking.
- Development of a user-friendly frontend interface using frameworks like React or Vue.js.
- Implementation of user authentication to personalize the experience.
- Enhanced error handling for API calls and data retrieval.
