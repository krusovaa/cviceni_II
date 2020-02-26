import json


class Object(object):
    def __init__(self, type):
        self.type = type

    def to_json(self):
        return {"type": self.type}


class Geometry(Object):
    def __init__(self, type, coordinates):
        super().__init__(type)
        self.coordinates = coordinates

    def to_json(self):
        dic = super().to_json()
        dic["coordinates"] = self.coordinates
        return dic
        # premisteno sem z point in linestring, protoze oboje dedi z geometry, tak to muzu presunout vys
        # malokdy vyse nez o jednoho predka


class Feature(Object):
    def __init__(self, geometry, properties, id=None):
        super().__init__("Feature")
        if not isinstance(geometry, Geometry):
            raise ValueError("Attempted to insert non Geometry as a geometry")
        self.geometry = geometry
        if id:
            self.id = id
        self.properties = properties

    def to_json(self):
        dic = super().to_json()
        dic["geometry"] = self.geometry.to_json()  # objekt typu geometry
        dic["properties"] = self.properties  # properties je slovnik
        return dic
        # return {"type": "Feature", "geometry": self.geometry.to_json(),     "properties": self.properties}


class FeatureCollection(Object):
    def __init__(self, features):
        super().__init__("FeatureCollection")
        self.features = features

    def to_json(self):
        dic = super().to_json()
        features = [f.to_json() for f in self.features]
        dic["features"] = features
        return dic
        # return {"type": "FeatureCollection", "features": features}


class Point(Geometry):
    def __init__(self, x, y, z=None):
        if z is not None:
            super().__init__("Point", [x, y, z])
        else:
            super().__init__("Point", [x, ])


class LineString(Geometry):
    def __init__(self, coords):
        super().__init__("LineString", coords)


class Polygon(Geometry):
    def __init__(self, coords):
        super().__init__("polygon", coords)


p = Point(10, 10)
print(json.dumps(p.to_json()))
f = Feature(p, {"test": "value"})
print(json.dumps(f.to_json()))
print(f.geometry.coordinates)
