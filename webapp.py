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
	if 'user' not in login_session: 
		return render_template('home1.html', recipes = recipes)
	else:
		return render_template('home2.html', recipes = recipes)

@app.route('/all_recipes')
def all_recipes():
	recipes = session.query(Recipe).all()
	return render_template('all_recipes.html', recipes = recipes)

def verify_password(email, password):
	user = session.query(User).filter_by(email=email).first()
	if not user or not user.verify_password(password):
		return False
	g.user = user
	return True



@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('log_in.html')
	elif request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		if email is None or password is None:
			flash('Missing Arguments')
			return redirect(url_for('login'))
		if verify_password(email, password):
			user = session.query(User).filter_by(email=email).one()
			flash('Login Successful, welcome {{user.name}}')
			login_session['name'] = user.name
			login_session['email'] = user.email
			login_session['id'] = user.id
			return redirect(url_for('home'))
		else:
			# incorrect username/password
			flash('Incorrect username/password combination')
			return redirect(url_for('login'))

@app.route('/sign_up', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        if name is None or email is None or password is None:
            flash("Your form is missing arguments")
            return redirect(url_for('sign_up'))
        if session.query(User).filter_by(email = email).first() is not None:
            flash("A user with this email address already exists")
            return redirect(url_for('sign_up'))
        user = User(name = name, email = email, password_hash = password)
        #User.hash_password(password)
        session.add(user)
        session.commit()
        flash("User Created Successfully!")
        return redirect(url_for('home'))
    else:
		return render_template('sign_up.html')


@app.route('/recipe/<int:recipe_id>')
def recipe(recipe_id):
	recipe = session.query(Recipe).filter_by(id=recipe_id).one()
	return render_template('recipe.html', recipe = recipe)

@app.route('/about')
def about():
	return render_template('about.html')





if __name__ == "__main__":
	app.run(debug = True)
