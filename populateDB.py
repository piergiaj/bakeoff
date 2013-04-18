#!/usr/bin/env python
import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recipe.settings")
from appRecipe.models import Recipe, Chef, Ingredient, UnitOfMeasure, RecipeIngredient, Instruction, ChefPicture

os.system("python manage.py rebuild_index")

#Chefs
#chefErik = Chef.objects.create(name='Erik',email='sanderej@rose-hulman.edu',password='bakeoff')
#chefAJ = Chef.objects.create(name='AJ',email='piergiaj@rose-hulman.edu',password='bakeoff')

chefErik = Chef.objects.create_user('Erik','sanderej@rose-hulman.edu','bakeoff')
chefAJ = Chef.objects.create_user('AJ','piergiaj@rose-hulman.edu','bakeoff')
chefFelisha = Chef.objects.create_user('Felisha','sanderej@rose-hulman.edu','bakeoff')
chefTrevor = Chef.objects.create_user('Trevor','piergiaj@rose-hulman.edu','bakeoff')
chefKice = Chef.objects.create_user('Kice','sanderej@rose-hulman.edu','bakeoff')
chefAlex = Chef.objects.create_user('Alex','piergiaj@rose-hulman.edu','bakeoff')
chefJosh = Chef.objects.create_user('Josh','piergiaj@rose-hulman.edu','bakeoff')

#Chef Pictures
ChefPicture.objects.create(chef=chefErik,path='https://file.ac/we4igBOMnuc/erik.jpg')
ChefPicture.objects.create(chef=chefAJ,path='https://file.ac/sCJYAvF3_BA/aj.jpg')
ChefPicture.objects.create(chef=chefFelisha,path='https://file.ac/we4igBOMnuc/erik.jpg')
ChefPicture.objects.create(chef=chefTrevor,path='https://file.ac/sCJYAvF3_BA/trevor.jpg')
ChefPicture.objects.create(chef=chefKice,path='https://file.ac/we4igBOMnuc/erik.jpg')
ChefPicture.objects.create(chef=chefAlex,path='https://file.ac/sCJYAvF3_BA/alex.jpg')
ChefPicture.objects.create(chef=chefJosh,path='https://file.ac/sCJYAvF3_BA/josh.jpg')

#Ingredients
ingPep = Ingredient.objects.create(name='Pepperoni')
ingMoz = Ingredient.objects.create(name='Mozzarella')
ingCru = Ingredient.objects.create(name='Crust')

ingCow = Ingredient.objects.create(name='Cow')

cinnIngs = []
ingMilk = Ingredient.objects.create(name='Milk')
ingEggs = Ingredient.objects.create(name='Eggs')
ingMarg = Ingredient.objects.create(name='Margarine')
ingBF = Ingredient.objects.create(name='Bread Flour')
ingSalt = Ingredient.objects.create(name='Salt')
ingWhiteSugar = Ingredient.objects.create(name='White Sugar')
ingBreadMachineYeast = Ingredient.objects.create(name='Bread Machine Yeast')
ingGC = Ingredient.objects.create(name='Ground Cinnamon')
ingButter = Ingredient.objects.create(name='Butter')
ingCreamCheese = Ingredient.objects.create(name='Cream Cheese')
ingCS = Ingredient.objects.create(name='Confectioners\' Sugar')
ingVE = Ingredient.objects.create(name='Vanilla Extract')
ingBS = Ingredient.objects.create(name='Brown Sugar')

#Units of measure
units = ('ounce','cup','pint','quart','gallon','teaspoon','tablespoon','pinch','piece','package')
for unit in units:
  u = UnitOfMeasure.objects.create(name=unit)

#Recipes
recPiz = chefErik.recipe_set.create(name='Pizza',chefComment='Bibidy Boppody',prepTime=10,cookTime=20)
recBee = chefAJ.recipe_set.create(name='Beef',chefComment='Awesome roast beef',prepTime=40,cookTime=90)
recCin = chefErik.recipe_set.create(name='Clone of a Cinnabon',chefComment='You have got to try these. The first time I made them, I thought of how much money I could save by making my own!',prepTime=20,cookTime=15)
recPas = chefErik.recipe_set.create(name='Pasta',chefComment='Bibidy Boppody Boo',prepTime=10,cookTime=20)
recLas = chefErik.recipe_set.create(name='Lasagna',chefComment='Bibidy Boppody, Boppody Boo',prepTime=10,cookTime=20)
recRoot = chefErik.recipe_set.create(name='TestRoot',chefComment='Bibidy Boppody, Boppody Boo',prepTime=10,cookTime=20)
recC1 = chefErik.recipe_set.create(name='TestChildOne',chefComment='Bibidy Boppody, Boppody Boo',prepTime=10,cookTime=20)
recC2 = chefErik.recipe_set.create(name='TestChildTwo',chefComment='Bibidy Boppody, Boppody Boo',prepTime=10,cookTime=20)
recC2.previousVersion = recC1
recC2.save()
recC1.previousVersion = recRoot
recC1.save()

#Instructions
recPiz.instruction_set.create(text='Put the dough down.')
recPiz.instruction_set.create(text='Put on some sauce.')
recPiz.instruction_set.create(text='Put on cheese.')
recPiz.instruction_set.create(text='Put on some pepperoni.')
recPiz.instruction_set.create(text='Bake for 20 minutes at 350.')

recCin.instruction_set.create(text='Place ingredients in the pan of the bread machine in the order recommended by the manufacturer. Select dough cycle; press Start.')
recCin.instruction_set.create(text='After the dough has doubled in size turn it out onto a lightly floured surface, cover and let rest for 10 minutes. In a small bowl, combine brown sugar and cinnamon.')
recCin.instruction_set.create(text='Roll dough into a 16x21 inch rectangle. Spread dough with 1/3 cup butter and sprinkle evenly with sugar/cinnamon mixture. Roll up dough and cut into 12 rolls. Place rolls in a lightly greased 9x13 inch baking pan. Cover and let rise until nearly doubled, about 30 minutes. Meanwhile, preheat oven to 400 degrees F (200 degrees C).')
recCin.instruction_set.create(text='Bake rolls in preheated oven until golden brown, about 15 minutes. While rolls are baking, beat together cream cheese, 1/4 cup butter, confectioners\' sugar, vanilla extract and salt. Spread frosting on warm rolls before serving.')

#Recipe Ingredients
RecipeIngredient.objects.create(recipe=recPiz,ingredient=ingPep,amount=10,unit=UnitOfMeasure.objects.get(name='piece'))
RecipeIngredient.objects.create(recipe=recPiz,ingredient=ingMoz,amount=3,unit=UnitOfMeasure.objects.get(name='cup'))
RecipeIngredient.objects.create(recipe=recPiz,ingredient=ingCru,amount=1,unit=UnitOfMeasure.objects.get(name='piece'))

RecipeIngredient.objects.create(recipe=recBee,ingredient=ingCow,amount=1,unit=UnitOfMeasure.objects.get(name='piece'))

RecipeIngredient.objects.create(recipe=recCin,ingredient=ingMilk,amount=1,unit=UnitOfMeasure.objects.get(name='cup'))
RecipeIngredient.objects.create(recipe=recCin,ingredient=ingEggs,amount=2,unit=UnitOfMeasure.objects.get(name='piece'))
RecipeIngredient.objects.create(recipe=recCin,ingredient=ingMarg,amount=.33,unit=UnitOfMeasure.objects.get(name='cup'))
RecipeIngredient.objects.create(recipe=recCin,ingredient=ingBF,amount=4.5,unit=UnitOfMeasure.objects.get(name='cup'))
RecipeIngredient.objects.create(recipe=recCin,ingredient=ingSalt,amount=1.125,unit=UnitOfMeasure.objects.get(name='teaspoon'))
RecipeIngredient.objects.create(recipe=recCin,ingredient=ingWhiteSugar,amount=.5,unit=UnitOfMeasure.objects.get(name='cup'))
RecipeIngredient.objects.create(recipe=recCin,ingredient=ingBreadMachineYeast,amount=2.5,unit=UnitOfMeasure.objects.get(name='teaspoon'))
RecipeIngredient.objects.create(recipe=recCin,ingredient=ingGC,amount=2.5,unit=UnitOfMeasure.objects.get(name='tablespoon'))
RecipeIngredient.objects.create(recipe=recCin,ingredient=ingButter,amount=.5,unit=UnitOfMeasure.objects.get(name='cup'))
RecipeIngredient.objects.create(recipe=recCin,ingredient=ingCreamCheese,amount=3,unit=UnitOfMeasure.objects.get(name='ounce'))
RecipeIngredient.objects.create(recipe=recCin,ingredient=ingCS,amount=1.5,unit=UnitOfMeasure.objects.get(name='cup'))
RecipeIngredient.objects.create(recipe=recCin,ingredient=ingVE,amount=.5,unit=UnitOfMeasure.objects.get(name='teaspoon'))
RecipeIngredient.objects.create(recipe=recCin,ingredient=ingBS,amount=1,unit=UnitOfMeasure.objects.get(name='cup'))


#Recipe Pictures
recPiz.recipepicture_set.create(path='https://file.ac/c868cDYjWdU/th.jpg')
recPicPiz = recPiz.recipepicture_set.create(path='https://file.ac/-QPcodr3qxs/pizza.jpg')
recPiz.mainPicture = recPicPiz
recPiz.save()

recPicBee = recBee.recipepicture_set.create(path='https://file.ac/YSu901Am9qY/beef.jpg')
recBee.mainPicture = recPicBee
recBee.save()

recPicCin = recCin.recipepicture_set.create(path='https://file.ac/lw9SLcwmIak/cinnabon.jpg')
recCin.mainPicture = recPicCin
recCin.save()

#Recipe ratings
recPiz.review(chef=chefAJ,comment="Best pizza ever!",rating=10)
recPiz.review(chef=chefFelisha,comment="Would be better without pepperoni.",rating=3)
recPiz.review(chef=chefTrevor,comment="Too greasy for me...",rating=1)
recPiz.review(chef=chefKice,comment="Great",rating=8)
recPiz.review(chef=chefAlex,comment="Amazing",rating=10)
recPiz.review(chef=chefJosh,comment="Good",rating=6)

recCin.review(chef=chefAJ,comment="Very good recipe",rating=10)
recCin.review(chef=chefFelisha,comment="Came out just like the Picture!",rating=10)
recCin.review(chef=chefTrevor,comment="Great dessert.",rating=8)
recCin.review(chef=chefAlex,comment="Amazing",rating=10)
recCin.review(chef=chefJosh,comment="Pretty good stuff",rating=9)

os.system("python manage.py rebuild_index")
