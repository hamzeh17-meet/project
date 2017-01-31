from databases import *
entries = session.query(Recipe).all()
for entry in entries:
	session.delete(entry)
session.commit()

recipe_names = ['klajlajo']
recipe_photos = ['https://static.pexels.com/photos/33045/lion-wild-africa-african.jpg']
recipe_ingredients = ['iasjdlkjoiasdklj,isjaoifjdoiasj']
recipe_how_to = ['klasdjfkajsoiflksaj']

for i in range(len(recipe_names)):
	recipe = Recipe(name = recipe_names[i], photo = recipe_photos[i], ingredients = recipe_ingredients[i], how_to = recipe_how_to[i])
	session.add(recipe)
	session.commit()


print("Done")
