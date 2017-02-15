from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func
from passlib.apps import custom_app_context as pwd_context
import random, string

Base = declarative_base()


class Recipe(Base):
	__tablename__ = 'recipe'
	id = Column(Integer, primary_key = True)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship('User', foreign_keys = [user_id])
	name = Column(String)
	ingredients = Column(String)
	photo = Column(String)
	how_to = Column(String)

	def set_photo(self, photo):
		self.photo = photo

class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key = True)
	recipe_id = Column(Integer, ForeignKey('recipe.id'))
	name = Column(String)
	email = Column(String, unique = True)
	password_hash = Column(String)
	recipes = relationship('Recipe', foreign_keys = [recipe_id])

	# def hash_password(self, password):
	# 	self.password_hash = pwd_context.encrypt(password)

	def verify_password(self, password):
		#return pwd_context.verify(password, self.password_hash)	
		return password == self.password_hash







engine = create_engine('sqlite:///foodrecipes.db')
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()
