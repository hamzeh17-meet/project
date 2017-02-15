from databases import *
entries = session.query(Recipe).all()
for entry in entries:
	session.delete(entry)
session.commit()

recipe_names = ["Watermelon & feta salad", "Black & blushing Worcestershire fillet"]#, "Salmon & pesto-dressed veg"]
recipe_photos = ["http://cdn.jamieoliver.com/recipe-database/xtra_med/APCAAduHaNaBC3zLiKa9yh.jpg", "http://cdn.jamieoliver.com/recipe-database/xtra_med/6lDzuPgHqWb9KSAdJ0JU31.jpg"]#, "http://cdn.jamieoliver.com/recipe-database/xtra_med/5p9W_lsfaXkAqPVhKib0AR.jpg"]
recipe_ingredients = ["700 g watermelon, 1 small red onion, 180 g feta cheese, 1 bunch of fresh mint, extra virgin olive oil", "600-700 piece of fillet steak, 2 heaped teaspoons French mustard, 8-10 tablespoons Worcestershire sauce , plus extra for drizzling, a good drizzle of extra virgin olive oil , plus extra to serve, 2 sprigs of fresh rosemary, unsalted butter, olive oil, thyme and rosemary flowers , optional"]


for i in range(len(recipe_names)):
	recipe = Recipe(name = recipe_names[i], photo = recipe_photos[i], ingredients = recipe_ingredients[i])
	session.add(recipe)
session.commit()


print("Done")
