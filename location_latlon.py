from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='location_application')
location = geolocator.geocode("paris")
print(location.address)
print((location.latitude, location.longitude))
