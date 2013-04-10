#!/usr/bin/env python
import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recipe.settings")
from appRecipe.models import Recipe, Chef, Ingredient

#Chefs
chefErik = Chef(name='Erik',email='sanderej@rose-hulman.edu',password='bakeoff')
chefErik.save()
chefAJ = Chef(name='AJ',email='piergiaj@rose-hulman.edu',password='bakeoff')
chefAJ.save()

#Ingredients
ingPep = Ingredient(name='Pepperoni')
ingPep.save()
ingMoz = Ingredient(name='Mozzarella')
ingMoz.save()
ingCru = Ingredient(name='Crust')
ingCru.save()

ingCow = Ingredient(name='Cow')
ingCow.save()

#Recipes
recPiz = chefErik.recipe_set.create(name='Pizza')
recPiz.ingredients.add(ingPep)
recPiz.ingredients.add(ingMoz)
recPiz.ingredients.add(ingCru)

recBee = chefAJ.recipe_set.create(name='Beef')
recBee.ingredients.add(ingCow)

#Recipe Pictures
recPicPiz = recPiz.recipepicture_set.create(path='https://file.ac/-QPcodr3qxs/pizza.jpg')
recPiz.mainPicture = recPicPiz
recPiz.save()

recPicBee = recBee.recipepicture_set.create(path='https://file.ac/YSu901Am9qY/beef.jpg')
recBee.mainPicture = recPicBee
recBee.save()