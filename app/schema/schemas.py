from flask_marshmallow import Marshmallow

ma = Marshmallow()

#User Schema
class RestauranteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'rating', 'name', 'site', 'email', 'phone', 'street', 'city', 'state', 'lat', 'lng')

class CoordinatesSchema(ma.Schema):
    class Meta:
        fields = ('count', 'avg', 'stddv')

restaurantes_schema = RestauranteSchema(many=True)
coordinates_schema = CoordinatesSchema()