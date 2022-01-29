from flask_marshmallow import Marshmallow

ma = Marshmallow()

#User Schema
class RestauranteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'rating', 'name', 'site', 'email', 'phone', 'street', 'city', 'state', 'lat', 'lng')

restaurante_schema = RestauranteSchema()
restaurantes_schema = RestauranteSchema(many=True)