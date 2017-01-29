from databases import *

recipe_names = ['klajlajo']
recipe_photos = ['https://static.pexels.com/photos/33045/lion-wild-africa-african.jpg']


for i in range(len(recipe_names)):
	recipe = Recipe(name = recipe_names[i], photo = recipe_photos[i])
	session.add(recipe)
	session.commit()


print("Done")