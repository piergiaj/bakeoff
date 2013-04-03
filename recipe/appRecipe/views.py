from django.http import HttpResponse, Http404
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404 #, get_list_or_404

from appRecipe.models import Recipe

def recipeIndex(request):
  recipe_list = Recipe.objects.all()
  template = loader.get_template('recipe/recipeIndex.html')
  context = { 'recipe_list': recipe_list,}
  return render(request, 'recipe/recipeIndex.html',context)
  
def recipeDetail(request, recipe_id):
  recipe = get_object_or_404(Recipe, pk=recipe_id)
  return render(request, 'recipe/recipeDetail.html', {'recipe':recipe})
  
def recipeIngredients(request, recipe_id):
  return HttpResponse("You're looking at the ingredients for recipe %s." % recipe_id)