from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404 #, get_list_or_404
from appRecipe.models import Recipe, Chef, RecipePicture
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from appRecipe import forms

from smartfile import BasicClient

import Image
#import zlib

def home(request):
  recipe_list = Recipe.objects.all()
  chef_list = Chef.objects.all()
  recipe_picture_list = RecipePicture.objects.all()
  context = { 'chef_list' : chef_list,
              'recipe_list': recipe_list,
              'recipe_picture_list' : recipe_picture_list, }
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

def getPic(request, pic_name):
  api = BasicClient('VATx6OASrU4KYLaWshrxIvyyYUIl8x','xkpKJ3Wti1cXilKJYnMSqaOLvmNnwe')
  pic = api.get('/path/data/images/',pic_name)
  #img = zlib.decompress(pic.data, 16+zlib.MAX_WBITS)
  img = pic.data
  response = HttpResponse(img, content_type='image')
  return response

def addChef(request):
  if request.method == 'POST':
    form = forms.AddChef(request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']

      chef = Chef(name=name, email=email, password=password)
      chef.save()

      return HttpResponseRedirect('/chefs')
  else:
    form = forms.AddChef()
  return render(request, 'recipe/addChef.html', {'form':form})

''' unused because using django's login function in urls
def login(request):
  if request.method == 'POST':
    form = forms.Login(request.POST, request.FILES)
    if form.is_valid():
      username = form.cleaned_data['username']
      pw = form.cleaned_data['password']

      try:
        chef = Chef.objects.get(name=username)
      except ObjectDoesNotExist:
        return HttpResponseRedirect('/login')

      if chef.password == pw:
        request.session['username'] = username
      else:
        return HttpResponseRedirect('/login')
    return HttpResponseRedirect('/')

  else:
    form = forms.Login()
  return render(request, 'recipe/awefawef.html', {'form':form})'''

@login_required(login_url='/login/')
def addRecipe(request):
  if request.method == 'POST':
    form = forms.AddRecipe(request.POST, request.FILES, extra=request.POST.get('inst'))
    if form.is_valid():
      recipeName = form.cleaned_data['recipe_Name']
      prepTime = form.cleaned_data['prep_Time']
      cookTime = form.cleaned_data['cook_Time']
      comments = form.cleaned_data['comments']
      
      instructions = form.cleaned_data['instructions']

      picData = request.FILES['picture'].read()
      picName = request.FILES['picture'].name.split(".")
      f = open("tmp."+picName[-1], 'w')
      f.write(picData)
      f.close()

      im = Image.open("tmp."+picName[-1]) 
      size = 64, 64
      im.save(picName[0]+"."+picName[-1], "JPEG", quality=30)
      im.thumbnail(size, Image.ANTIALIAS)
      im.save("thumb.jpg", "JPEG")

      api = BasicClient('VATx6OASrU4KYLaWshrxIvyyYUIl8x','xkpKJ3Wti1cXilKJYnMSqaOLvmNnwe')

      

      #api.post('/path/data/images/', file=(recipeName+'.'+picName[-1], picData))

      recipe = Recipe.objects.create(chef=get_object_or_404(Chef, pk=1), name=recipeName, prepTime=prepTime, cookTime=cookTime, chefComment=comments)#TODO: add chef, picture, ingredients, etc
      
      recipe.instruction_set.create(text=instructions)
      for i in range(form.cleaned_data['inst']):
        inst = request.POST.get('extra_field_'+str(i))
        recipe.instruction_set.create(text=inst)

      #make folder for pictures
      pictureFolder = '/RecipePicture/'+str(recipe.id)+'/'
      api.post('/path/oper/mkdir',path=pictureFolder)

      #upload picture
      fileName = recipeName+'.'+picName[-1]
      api.post('/path/data'+pictureFolder, file=(fileName, open(picName[0]+"."+picName[-1], 'r').read()))
      api.post('/path/data'+pictureFolder, file=('thumb.jpg', open('thumb.'+picName[-1], 'r').read()))

      #make picture object
      rpic = recipe.recipepicture_set.create()
      rpic.setPath(fileName)
      rpic.setSmallPath('thumb.jpg')

      #set this pic as recipe's main pic
      recipe.mainPicture = rpic
      recipe.save()

      return HttpResponseRedirect('/recipes')
  else:
    form = forms.AddRecipe()
  return render(request, 'recipe/addRecipe.html', {'form':form})
