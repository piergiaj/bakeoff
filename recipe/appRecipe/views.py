from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404 #, get_list_or_404

from appRecipe.models import Recipe, Chef
from appRecipe import forms

def home(request):
  recipe_list = Recipe.objects.all()
  chef_list = Chef.objects.all()
  context = { 'chef_list' : chef_list,
              'recipe_list': recipe_list, }
  return render(request, 'recipe/home.html', context)

def recipeIndex(request):
  recipe_list = Recipe.objects.all()
  context = { 'recipe_list': recipe_list,}
  return render(request, 'recipe/recipeIndex.html',context)
  
def recipeDetail(request, recipe_id):
  recipe = get_object_or_404(Recipe, pk=recipe_id)
  return render(request, 'recipe/recipeDetail.html', {'recipe':recipe})
  
def recipeIngredients(request, recipe_id):
  return HttpResponse("You're looking at the ingredients for recipe %s." % recipe_id)

def chefIndex(request):
  chef_list = Chef.objects.all()
  context = { 'chef_list' : chef_list }
  return render(request, 'recipe/chefIndex.html', context)

def chefDetail(request, chef_id):
  chef = get_object_or_404(Chef, pk=chef_id)
  return render(request, 'recipe/chefDetail.html', {'chef':chef})

def addChef(request):
  if request.method == 'POST':
    form = forms.AddChef(request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']
      print password

      chef = Chef(name=name, email=email, password=password)
      chef.save()

      return HttpResponseRedirect('/chefs')
  else:
    form = forms.AddChef()
  return render(request, 'recipe/addChef.html', {'form':form})

def addRecipe(request):
  if request.method == 'POST':
    form = forms.AddChef(request.POST)
    if form.is_valid():
      recipeName = form.cleaned_data['recipeName']
      prepTime = form.cleaned_data['prepTime']
      cookTime = form.cleaned_data['cookTime']
      comments = form.cleaned_data['comments']
      picture = forms.cleaned_data['picture']
  else:
    form = forms.AddRecipe()
    return render(request, 'recipe/addRecipe.html', {'form':form})
 