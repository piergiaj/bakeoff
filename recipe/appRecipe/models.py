from django.db import models
from django.contrib.auth.models import User

from smartfile import BasicClient
from appRecipe import util

# Create your models here.
class Chef(User):
  dateCreated = models.DateTimeField(auto_now_add=True)

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
  dateCreated = models.DateTimeField(auto_now_add=True)
  #Relations
  mainPicture = models.ForeignKey('RecipePicture',blank=True,null=True, related_name = 'mainPictureForRecipe')
  chef = models.ForeignKey(Chef)
  previousVersion = models.ForeignKey('self',blank=True,null=True)
  ingredients = models.ManyToManyField(Ingredient, through=RecipeIngredient)

  def totalTime(self):
    return self.prepTime+self.cookTime

  def totalTimeString(self):
    return util.timeString(self.totalTime())

  def prepTimeString(self):
    return util.timeString(self.prepTime)

  def cookTimeString(self):
    return util.timeString(self.cookTime)
  
class Instruction(models.Model):
  text = models.CharField(max_length=500)
  #Relations
  recipe = models.ForeignKey(Recipe)

class Picture(models.Model):
  path = models.CharField(max_length=500)

  def setPath(self, fileName):
    api = BasicClient('VATx6OASrU4KYLaWshrxIvyyYUIl8x','xkpKJ3Wti1cXilKJYnMSqaOLvmNnwe')
    #creating link to picture
    response = api.post('/link',path='RecipePicture/'+str(self.recipe.id)+'/'+fileName,read=True)
    self.path = response['href']+fileName
    self.save()

class RecipePicture(Picture):
  #Relations
  recipe = models.ForeignKey(Recipe)
  
class ChefPicture(Picture):
  #Relations
  chef = models.ForeignKey(Chef)
  
class Review(models.Model):
  comment = models.CharField(max_length=500)
  rating = models.IntegerField()
  dateCreated = models.DateTimeField(auto_now_add=True)
  #Relations
  chef = models.ForeignKey(Chef)
  recipe = models.ForeignKey(Recipe)