from django.http import HttpResponse

def recipeIndex(request):
  return HttpResponse("Hello, world. You're at the recipe index.")
  
def recipeDetail(request, recipe_id):
  return HttpResponse("You're looking at recipe %s." % recipe_id)
  
def recipeIngredients(request, recipe_id):
  return HttpResponse("You're looking at the ingredients for recipe %s." % recipe_id)