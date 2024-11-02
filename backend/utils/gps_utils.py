def calculate_distance(coord1, coord2):
    """Calculate distance between two GPS coordinates (latitude, longitude)."""
    from geopy.distance import geodesic

    return geodesic(coord1, coord2).miles

def validate_coordinates(coords):
    """Validate if the given coordinates are within a valid range."""
    lat, lon = coords
    return -90 <= lat <= 90 and -180 <= lon <= 180
