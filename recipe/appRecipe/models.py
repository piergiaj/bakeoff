from django.db import models

# Create your models here.
class Ingredient(models.Model):
  name = models.CharField(max_length = 200)
  
class Recipe(models.Model):
  name = models.CharField(max_length=200)
  prepTime = models.IntegerField(blank=True,null=True)
  cookTime = models.IntegerField(blank=True,null=True)
  chefComment = models.CharField(max_length=500)
  #Relations
  mainPicture = models.ForeignKey('RecipePicture',blank=True,null=True, related_name = 'mainPictureForRecipe')
  chef = models.ForeignKey('Chef')
  previousVersion = models.ForeignKey('self',blank=True,null=True)
  ingredients = models.ManyToManyField(Ingredient)
  
class Instruction(models.Model):
  name = models.CharField(max_length=500)
  #Relations
  recipe = models.ForeignKey(Recipe)
  
class RecipePicture(models.Model):
  path = models.CharField(max_length=500)
  #Relations
  recipe = models.ForeignKey(Recipe)
  
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