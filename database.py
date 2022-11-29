import sqlite3
from app import db
conn = sqlite3.connect('weather.db')
#db.create_all()

#conn.execute('CREATE TABLE weather (name TEXT, addr TEXT, city TEXT, pin TEXT)')

conn.close()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisisasecret'
db = SQLAlchemy(app)

c = city.query.first()
db.session.delete(c)
db.session.commit()

