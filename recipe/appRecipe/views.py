from django.http import HttpResponse
from django.template import Context, loader

from appRecipe.models import Recipe

def recipeIndex(request):
  recipe_list = Recipe.objects.all()
  template = loader.get_template('recipe/recipeIndex.html')
  context = Context({
    'recipe_list': recipe_list,
  })
  return HttpResponse(template.render(context))
  
def recipeDetail(request, recipe_id):
  return HttpResponse("You're looking at recipe %s." % recipe_id)
  
def recipeIngredients(request, recipe_id):
  return HttpResponse("You're looking at the ingredients for recipe %s." % recipe_id)