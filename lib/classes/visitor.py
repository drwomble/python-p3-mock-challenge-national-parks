class Visitor:
    all = []
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)
        
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15 and not hasattr(self, '_name'):
            self._name = name
        else:
            raise Exception('name must be a string with 1 to 15 characters')
        
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor is self]
    
    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})
    
    
from classes.trip import Trip