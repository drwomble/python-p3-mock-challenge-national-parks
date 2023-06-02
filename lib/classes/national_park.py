class NationalPark:
    all = []
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)
        
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, '_name'):
            self._name = name
        else:
            raise Exception('name must be a string and cannot be renamed')
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]
    
    def visitors(self):
        return list({trip.visitor for trip in self.trips()})
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visitors = [trip.visitor for trip in self.trips()]
        return max(set(visitors), key=visitors.count)
    

from classes.trip import Trip
from classes.visitor import Visitor