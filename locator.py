from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


class Location():
    def __init__(self,location):
        self.locator = Nominatim(user_agent='weather_app')
        self.location = location
    def latitude(self):
        #returns latitude of location
        try: return self.locator.geocode(self.location).latitude
        except: return None
    def longitude(self):
        #returns longitude of location
        try: return self.locator.geocode(self.location).longitude
        except: return None


