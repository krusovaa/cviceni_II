import json


class Object(object):
    def __init__(self, type=None):
        self.type = type


class Geometry(Object):
    def __init__(self, type, coordinates=None):
        super().__init__(type)
        self.coordinates = coordinates


class Feature(Object):
    def __init__(self, geometry, properties, id=None):
        super().__init__('Feature')
        if not isinstance(geometry, Geometry):
            raise ValueError('Attempted to insert non Geometry as a geometry')
        self.geometry = geometry
        self.properties = properties
        if id:
            self.id = id

    def to_json(self):
        return {"type": "Feature", "geometry": self.geometry.to_json(), "prooperties": self.properties}
        #return '{{"geometry:{} }}'. format(self.geometry.to_json_str)
        #return json.dumps(json_obj)

class FeatureCollection(Object):
    def __init__(self, features):
        super().__init__('FeatureCollection')
        self.features = features


class Point(Geometry):
    def __init__(self, x, y, z=None):
        if z is not None:
            super().__init__('Point', [x, y, z])
        else:
            super().__init__('Point', [x, y])
    def to_json(self):
        return{"type": "Point", "coordinates": self.coordinates}
        # return '{{"type":"Point", "coordinates": {}}}'. format(self.coordinates)


class Linestring(Geometry):
    def __init__(self, type, coordinates):
        super().__init__(type, coordinates)
    pass


p = Point(10, 10)
print(json.dumps(p.to_json()))
f = Feature(p, {})
print(json.dumps(f.to_json()))
