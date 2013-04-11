#!/usr/bin/env python
import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recipe.settings")
from appRecipe.models import Recipe, Chef, Ingredient, UnitOfMeasure, RecipeIngredient

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

#Units of measure
units = ('ounce','cup','pint','quart','gallon','teaspoon','tablespoon','pinch','piece','package')
for unit in units:
  u = UnitOfMeasure(name=unit)
  u.save()

#Recipes
recPiz = chefErik.recipe_set.create(name='Pizza',chefComment='Bibidy Boppody')
recBee = chefAJ.recipe_set.create(name='Beef',chefComment='Awesome roast beef')

#Recipe Ingredients
riList = []
riList.append(RecipeIngredient(recipe=recPiz,ingredient=ingPep,amount=10,unit=UnitOfMeasure.objects.get(name='piece')))
riList.append(RecipeIngredient(recipe=recPiz,ingredient=ingMoz,amount=3,unit=UnitOfMeasure.objects.get(name='cup')))
riList.append(RecipeIngredient(recipe=recPiz,ingredient=ingCru,amount=1,unit=UnitOfMeasure.objects.get(name='piece')))

riList.append(RecipeIngredient(recipe=recBee,ingredient=ingCow,amount=1,unit=UnitOfMeasure.objects.get(name='piece')))
for ri in riList:
  ri.save()

#Recipe Pictures
recPicPiz = recPiz.recipepicture_set.create(path='https://file.ac/-QPcodr3qxs/pizza.jpg')
recPiz.mainPicture = recPicPiz
recPiz.save()

recPicBee = recBee.recipepicture_set.create(path='https://file.ac/YSu901Am9qY/beef.jpg')
recBee.mainPicture = recPicBee
recBee.save()