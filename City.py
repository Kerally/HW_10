import random
from pprint import pprint

class City:

    def __init__(self):
        self._city = []
        self._humans = 0


    def print_table(self):
        return self._city


    # set city value (streets, etc.)
    def city_fill(self):
        self._city = [
            {
                home:human 
                for home in range(1, random.randint(5, 20))
                for human in range(1, random.randint(1, 100))
            } 
            for street in range(5)
        ]


    # city property
    @property
    def city(self):
        return self._city
    

    @city.setter
    def city(self, value):
        self._city = value


    # street property
    @property
    def street(self):
        return self._city

    @street.setter
    def street(self, value):
        self._city.append(value)


    @street.deleter
    def street(self):
        del self._city


    # humans property
    @property
    def humans(self):
        for i in self.city: 
            for key, value in i.items():
                self._humans += value
        return self._humans


    @humans.setter
    def humans(self, value):
        self._humans = value


a = City()
a.city_fill()
del a.street[0]
del a.street[0]
pprint(a.street)

