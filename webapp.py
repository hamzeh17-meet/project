from flask import Flask
from databases import *

app = Flask(__name__)

engine = create_engine('sqlite:///foodrecipes.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()


@app.route('/')
def home():
	return "asjdoasS"
@app.route('/all_recipes')
def all():
	recipes = session.query(Recipe).all()
	






if __name__ == "__main__":
	app.run(debug = True)
