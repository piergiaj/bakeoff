from django.db import models

from smartfile import BasicClient

# Create your models here.
class Ingredient(models.Model):
  name = models.CharField(max_length = 200)

class UnitOfMeasure(models.Model):
  name = models.CharField(max_length=50) # Make these singular and use Django's pluralizations?

class RecipeIngredient(models.Model):
  amount = models.FloatField()
  #Relations
  unit = models.ForeignKey(UnitOfMeasure)
  ingredient = models.ForeignKey(Ingredient)
  recipe = models.ForeignKey('Recipe')
  
class Recipe(models.Model):
  name = models.CharField(max_length=200)
  prepTime = models.IntegerField(blank=True,null=True)
  cookTime = models.IntegerField(blank=True,null=True)
  chefComment = models.CharField(max_length=500)
  #Relations
  mainPicture = models.ForeignKey('RecipePicture',blank=True,null=True, related_name = 'mainPictureForRecipe')
  chef = models.ForeignKey('Chef')
  previousVersion = models.ForeignKey('self',blank=True,null=True)
  ingredients = models.ManyToManyField(Ingredient, through=RecipeIngredient)
  
class Instruction(models.Model):
  name = models.CharField(max_length=500)
  #Relations
  recipe = models.ForeignKey(Recipe)
  
class RecipePicture(models.Model):
  path = models.CharField(max_length=500)
  #Relations
  recipe = models.ForeignKey(Recipe)

  def setPath(self, fileName):
    api = BasicClient('VATx6OASrU4KYLaWshrxIvyyYUIl8x','xkpKJ3Wti1cXilKJYnMSqaOLvmNnwe')
    #creating link to picture
    response = api.post('/link',path='RecipePicture/'+str(self.recipe.id)+'/'+fileName,read=True)
    self.path = response['href']+fileName
    self.save()
  
class Chef(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField()
  password = models.CharField(max_length=500)
  
class Review(models.Model):
  comment = models.CharField(max_length=500)
  rating = models.IntegerField()
  #Relations
  chef = models.ForeignKey(Chef)
  recipe = models.ForeignKey(Recipe)