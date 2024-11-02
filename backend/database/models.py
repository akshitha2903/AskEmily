from database import mongo

class Campground(mongo.Document):
    name = mongo.StringField(required=True)
    location = mongo.StringField(required=True)
    amenities = mongo.ListField(mongo.StringField())
    rating = mongo.FloatField()

class RVTechnician(mongo.Document):
    name = mongo.StringField(required=True)
    location = mongo.StringField(required=True)
    services_offered = mongo.ListField(mongo.StringField())
