from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_bootstrap import Bootstrap


app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#db.create_all()

def create_tables():
    from app.db_handler import Beer
    
    
    beer = Beer()
    beer.name = "temp3"
    beer.val1 = 5
    beer.val2 = 5
    beer.val3 = 5
    beer.val4 = 5
    beer.val5 = 5
    beer.rarity = 3
    beer.abv = 123
    beer.pattern = 1
    beer.tap = -1
    db.session.add(beer)
    db.session.commit()

#create_tables()

from app import POS, db_handler
from app.arduino import get_ip

print("Current IP is", get_ip())
print("Point your browser to http://", get_ip(), sep="")
print()

#app.run(debug=True, host='0.0.0.0')
