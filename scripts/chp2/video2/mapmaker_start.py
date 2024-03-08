class Point():
    def __init__(self, name, latitude,longitude):

        if not (-90<= latitude <= 90) or not(-180 <= longitude <=180):
            print("I am here!!!")
            raise ValueError(f'Invalid value! LT: {latitude}, LO:{longitude}')
        print("I am here!!! 2222222")
        self._name = name
        self._latitude = latitude
        self._longitude = longitude
        
    def get_lat_long(self):
        return (self._latitude, self._longitude)
    
