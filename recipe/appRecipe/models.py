from django.db import models

# Create your models here.
class Ingredient(models.Model):
  name = models.CharField(max_length = 200)
  
class Recipe(models.Model):
  name = models.CharField(max_length=200)
  prepTime = models.IntegerField(default=0)
  cookTime = models.IntegerField(default=0)
  chefComment = models.CharField(max_length=500)
  #FK
  mainPicture = models.ForeignKey('RecipePicture', related_name = 'mainPictureForRecipe' )
  chef = models.ForeignKey('Chef')
  previousVersion = models.ForeignKey('self')
  ingredients = models.ManyToManyField(Ingredient)
  
class Instruction(models.Model):
  name = models.CharField(max_length=500)
  #FK
  recipe = models.ForeignKey(Recipe)
  
class RecipePicture(models.Model):
  path = models.CharField(max_length=500)
  #FK
  recipe = models.ForeignKey(Recipe)
  
class Chef(models.Model):
  name = models.CharField(max_length=200)
  
class Review(models.Model):
  comment = models.CharField(max_length=500)
  rating = models.IntegerField()
  #FK
  chef = models.ForeignKey(Chef)
  recipe = models.ForeignKey(Recipe)