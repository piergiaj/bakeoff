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

#Chef Pictures
ChefPicture.objects.create(chef=chefErik,path='https://file.ac/nV3ekIcqA24/erik.jpg',smallpath='https://file.ac/VTPzb5blA9U/erik_thumb.jpg')
ChefPicture.objects.create(chef=chefAJ,path='https://file.ac/UIP7896_klA/aj.jpg',smallpath='https://file.ac/AKGjKXHgrwo/aj_thumb.jpg')

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
ingCS = Ingredient.objects.create(name='Confectioners Sugar')
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
recCup = chefAJ.recipe_set.create(name='Easy Chocolate Cupcakes',chefComment='These chocolate cupcakes are easy to make and very tasty.',prepTime=10,cookTime=20)

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

recCup.instruction_set.create(text='Preheat oven to 350 degrees F (175 degrees C). Grease two muffin pans or line with 20 paper baking cups.')
recCup.instruction_set.create(text='In a medium bowl, beat the butter and sugar with an electric mixer until light and fluffy. Mix in the eggs, almond extract and vanilla. Combine the flour, cocoa, baking powder and salt; stir into the batter, alternating with the milk, just until blended. Spoon the batter into the prepared cups, dividing evenly.')
recCup.instruction_set.create(text='Bake in the preheated oven until the tops spring back when lightly pressed, 20 to 25 minutes. Cool in the pan set over a wire rack. When cool, arrange the cupcakes on a serving platter. Frost with your favorite frosting.')

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

RecipeIngredient.objects.create(recipe=recCup,ingredient=ingButter,amount=10,unit=UnitOfMeasure.objects.get(name='tablespoon'))
RecipeIngredient.objects.create(recipe=recCup,ingredient=ingWhiteSugar,amount=1.25,unit=UnitOfMeasure.objects.get(name='cup'))
RecipeIngredient.objects.create(recipe=recCup,ingredient=ingEggs,amount=4,unit=UnitOfMeasure.objects.get(name='piece'))
RecipeIngredient.objects.create(recipe=recCup,ingredient=Ingredient.objects.create(name='Almond Extract'),amount=.25,unit=UnitOfMeasure.objects.get(name='teaspoon'))
RecipeIngredient.objects.create(recipe=recCup,ingredient=Ingredient.objects.create(name='Vanilla Extract'),amount=1,unit=UnitOfMeasure.objects.get(name='teaspoon'))
RecipeIngredient.objects.create(recipe=recCup,ingredient=Ingredient.objects.create(name='All-Purpose Flour'),amount=1.5,unit=UnitOfMeasure.objects.get(name='cup'))
RecipeIngredient.objects.create(recipe=recCup,ingredient=Ingredient.objects.create(name='Unsweetened Cocoa Powder'),amount=.75,unit=UnitOfMeasure.objects.get(name='teaspoon'))
RecipeIngredient.objects.create(recipe=recCup,ingredient=Ingredient.objects.create(name='Baking Powder'),amount=2,unit=UnitOfMeasure.objects.get(name='teaspoon'))
RecipeIngredient.objects.create(recipe=recCup,ingredient=ingSalt,amount=.25,unit=UnitOfMeasure.objects.get(name='teaspoon'))
RecipeIngredient.objects.create(recipe=recCup,ingredient=ingMilk,amount=.75,unit=UnitOfMeasure.objects.get(name='cup'))


#Recipe Pictures
recPiz.recipepicture_set.create(path='https://file.ac/wxkntoCINNU/th.jpg',smallpath='https://file.ac/LqQxM0DIrUI/th_thumb.jpg')
recPicPiz = recPiz.recipepicture_set.create(path='https://file.ac/egpifGACgq4/pizza.jpg',smallpath='https://file.ac/ZD_Dlo0XjhM/pizza_thumb.jpg')
recPiz.mainPicture = recPicPiz
recPiz.save()

recPicBee = recBee.recipepicture_set.create(path='https://file.ac/h6SbdWbQFqo/beef.jpg',smallpath='https://file.ac/tjBg7qSi8lk/beef_thumb.jpg')
recBee.mainPicture = recPicBee
recBee.save()

recPicCin = recCin.recipepicture_set.create(path='https://file.ac/_HclFvSV9kQ/cinnabon.jpg',smallpath='https://file.ac/IK8HbozIrm4/cinnabon_thumb.jpg')
recCin.mainPicture = recPicCin
recCin.save()

recPicCup = recCup.recipepicture_set.create(path='https://file.ac/WEgTe41xYIg/cupcake.jpg',smallpath='https://file.ac/k1OPo0EG4q0/cupcake_thumb.jpg')
recCup.mainPicture = recPicCup
recCup.save()

#Recipe ratings
recPiz.review(chef=chefAJ,comment="Best pizza ever!",rating=10)

recBee.review(chef=chefErik,comment="Didn't look like the best recipe, but I tried it and it was good!",rating=8)

recCin.review(chef=chefAJ,comment="Very good recipe",rating=9)

recCup.review(chef=chefErik,comment="Good enough to enter in a Bake-Off!",rating=10)

os.system("python manage.py rebuild_index")
