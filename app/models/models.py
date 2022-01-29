from database import db

class Restaurante(db.Model):
    __tablename__ = 'restaurantes'
    id = db.Column(db.String(40), primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(40), nullable=False)
    site = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(40), nullable=False)
    lat = db.Column(db.Numeric, nullable=False)
    lng = db.Column(db.Numeric, nullable=False)

    def __init__(self, id, rating, name, site, email, phone, street, city, state, lat, lng):
        self.id = id
        self.rating = rating
        self.name = name
        self.site = site
        self.email = email
        self.phone = phone
        self.street = street
        self.city = city
        self.state = state
        self.lat = lat
        self.lng = lng