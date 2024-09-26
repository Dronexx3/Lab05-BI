from geopy.geocoders import Nominatim
geolocator = Nominatim (user_agent="geo_app")
location = geolocator.geocode("1600 Amphitheatre Parkway, Mountain View, CA")
print(location.address)
# Geocodificación inversa
location = geolocator.reverse ("37.4221, -122.0841")
print(location.address)