

class Point():
    def __init__(self, name, latitude, longitude):
        if not isinstance(name,str):
            raise TypeError("Invalid type! Provide string")
        self.name = name

        if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
            raise ValueError("Invalid latitude, longitude combination.")
        self.latitude = latitude
        self.longitude = longitude

    def __eq__(self, other):
        return self.name == other.name and self.latitude == other.latitude and self.longitude == other.longitude

    def get_lat_long(self):
        return (self.latitude, self.longitude)


class Map():
    def __init__(self, name):
        self.name = name
        self.pointsList= []
        
    def add_point(self, newPoint: Point):
        if newPoint in self.pointsList:
            raise ValueError("Point already exists!")
        self.pointsList.append(newPoint)

    def get_points(self):
        return self.pointsList   