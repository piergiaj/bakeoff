#!/usr/bin/env python
import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recipe.settings")
from appRecipe.models import Recipe, Chef, Ingredient, UnitOfMeasure, RecipeIngredient, Instruction

#Chefs
#chefErik = Chef.objects.create(name='Erik',email='sanderej@rose-hulman.edu',password='bakeoff')
#chefAJ = Chef.objects.create(name='AJ',email='piergiaj@rose-hulman.edu',password='bakeoff')

chefErik = Chef.objects.create_user('Erik','sanderej@rose-hulman.edu','bakeoff')
chefAJ = Chef.objects.create_user('AJ','piergiaj@rose-hulman.edu','bakeoff')

#Chef Pictures
chefErik.chefpicture_set.create(path='https://file.ac/we4igBOMnuc/erik.jpg')
chefAJ.chefpicture_set.create(path='https://file.ac/sCJYAvF3_BA/aj.jpg')

#Ingredients
ingPep = Ingredient.objects.create(name='Pepperoni')
ingMoz = Ingredient.objects.create(name='Mozzarella')
ingCru = Ingredient.objects.create(name='Crust')

ingCow = Ingredient(name='Cow')
ingCow.save()

#Units of measure
units = ('ounce','cup','pint','quart','gallon','teaspoon','tablespoon','pinch','piece','package')
for unit in units:
  u = UnitOfMeasure.objects.create(name=unit)

#Recipes
recPiz = chefErik.recipe_set.create(name='Pizza',chefComment='Bibidy Boppody',prepTime=10,cookTime=20)
recBee = chefAJ.recipe_set.create(name='Beef',chefComment='Awesome roast beef',prepTime=40,cookTime=90)

#Instructions
recPiz.instruction_set.create(text='Put the dough down.')
recPiz.instruction_set.create(text='Put on some sauce.')
recPiz.instruction_set.create(text='Put on cheese.')
recPiz.instruction_set.create(text='Put on some pepperoni.')
recPiz.instruction_set.create(text='Bake for 20 minutes at 350.')

#Recipe Ingredients
RecipeIngredient.objects.create(recipe=recPiz,ingredient=ingPep,amount=10,unit=UnitOfMeasure.objects.get(name='piece'))
RecipeIngredient.objects.create(recipe=recPiz,ingredient=ingMoz,amount=3,unit=UnitOfMeasure.objects.get(name='cup'))
RecipeIngredient.objects.create(recipe=recPiz,ingredient=ingCru,amount=1,unit=UnitOfMeasure.objects.get(name='piece'))

RecipeIngredient.objects.create(recipe=recBee,ingredient=ingCow,amount=1,unit=UnitOfMeasure.objects.get(name='piece'))


#Recipe Pictures
recPiz.recipepicture_set.create(path='https://file.ac/c868cDYjWdU/th.jpg')
recPicPiz = recPiz.recipepicture_set.create(path='https://file.ac/-QPcodr3qxs/pizza.jpg')
recPiz.mainPicture = recPicPiz
recPiz.save()

recPicBee = recBee.recipepicture_set.create(path='https://file.ac/YSu901Am9qY/beef.jpg')
recBee.mainPicture = recPicBee
recBee.save()


os.system("manage.py rebuild_index")