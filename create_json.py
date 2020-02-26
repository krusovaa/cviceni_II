import json


class Object(object):
    def __init__(self, type):
        self.type = type

    def to_json(self):
        return {"type": self.type}


class Geometry(Object):
    @classmethod
    def from_json(cls, adict):
        if adict["type"] == "LineString":
            obj = LineString.from_json(adict)
        elif adict["type"] == "Point":
            obj = Point.from_json(adict)
        elif adict["type"] == "Polygon":
            obj = Polygon.from_json(adict)
        return obj

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
    @classmethod
    def from_json(cls, adict):
        properties = adict["properties"]
        geometry = Geometry.from_json(adict["geometry"])
        obj = cls(geometry, properties)
        return obj

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
    @classmethod
    def from_json(cls, adict):  # cls zkratka nasi class (tady FeatureCollection)
        feature_objs = []
        for fdict in adict["features"]:
            fobj = Feature.from_json(fdict)
            feature_objs.append(fobj)
        obj = cls(feature_objs)  # ekvivalentni FeatureColection(feature_objs)
        return obj

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
    @classmethod
    def from_json(cls, adict):
        coord_x = adict["coordinates"][0]
        coord_y = adict["coordinates"][1]
        obj = cls(coord_x, coord_y)
        return obj

    def __init__(self, x, y, z=None):
        if z is not None:
            super().__init__("Point", [x, y, z])
        else:
            super().__init__("Point", [x, y])


class LineString(Geometry):
    @classmethod
    def from_json(cls, adict):
        coords = adict["coordinates"]
        obj = cls(coords)
        return obj

    def __init__(self, coords):
        super().__init__("LineString", coords)


class Polygon(Geometry):
    @classmethod
    def from_json(cls, adict):
        coords = adict["coordinates"]
        obj = cls(coords)
        return obj

    def __init__(self, coords):
        super().__init__("polygon", coords)


def from_json(adict):
    if adict["type"] == "FeatureCollection":
        return FeatureCollection.from_json(adict)
    elif adict["type"] == "Feature":
        return Feature.from_json(adict)
    elif adict["type"] == "Geometry":
        return Point.from_json(adict)
    else:
        print("Unknown type {}".format(adict["type"]))

    # zjisti co je to zac
    # vytvori oibjektovou hierarchii
    # vrati korenovy element (Feature / Feature Collection / Geometry)


# FeatureCollection.from_json(None)
p = Point(10, 10)
# print(json.dumps(p.to_json()))
f = Feature(p, {"test": "value"})
# print(json.dumps(f.to_json()))
# print(f.geometry.coordinates)

with open("BEZ_ObjektMPP_b.json", 'r', encoding='utf-8') as f:
    adict = json.load(f)
print(adict)
print(from_json(adict).to_json())
