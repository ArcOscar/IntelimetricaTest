from flask import Flask
from database import db
from sqlalchemy_utils import create_database, database_exists
from routes.routes import blueprint

app = Flask(__name__)

# Database
db_usuario = 'root'
db_clave = 'RootRoot77'
db_host = 'localhost'
db_nombre = 'db_api_intelimetrica'

DB_URL = f'mysql+pymysql://{db_usuario}:{db_clave}@{db_host}/{db_nombre}'

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Initialize SQLAlchemy
db.init_app(app)

#Routes instance
app.register_blueprint(blueprint)

#Create db
with app.app_context():
    if not database_exists(DB_URL):
        create_database(DB_URL)
    db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)