
from flask import Flask, url_for, flash, render_template, redirect, request, g, send_from_directory
from flask import session as login_session
from databases import *
from werkzeug.utils import secure_filename
from flask import render_template

app = Flask(__name__)


app.secret_key = "Marvel is better than DC"
engine = create_engine('sqlite:///foodrecipes.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()


@app.route('/')
def home():
	recipes = session.query(Recipe).all()
	return render_template('home.html', recipes = recipes)


@app.route('/all_recipes')
def all():
	recipes = session.query(Recipe).all()
	return render_template('all_recipes.html', recipes = recipes)


@app.route('/login')
def login():
	return render_template('log_in.html')


@app.route('/sign_up')
def sign_up():
	return render_template('sign_up.html')


@app.route('/recipe/<int:recipe_id>')
def recipe_show(recipe_id):
	return render_template('recipe.html', recipe = recipe_id)







if __name__ == "__main__":
	app.run(debug = True)
