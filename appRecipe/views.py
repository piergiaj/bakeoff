from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404 #, get_list_or_404
from appRecipe.models import Recipe, Chef, RecipePicture, Ingredient, UnitOfMeasure, RecipeIngredient, Chef_favoriteRecipes
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from appRecipe import forms

from smartfile import BasicClient

from threading import Thread

import Image
import os
import sys
#import zlib

def home(request):
  recipe_list = Recipe.objects.all()
  chef_list = Chef.objects.all()
  recipe_picture_list = RecipePicture.objects.all()
  context = { 'chef_list' : chef_list,
              'recipe_list': recipe_list,
              'recipe_picture_list' : recipe_picture_list, }
  return render(request, 'recipe/home.html', context)

def recipeIndex(request, sortby = 'HighestRated'):
  if sortby == 'Newest':
    recipe_list = Recipe.objects.all().order_by('id').reverse()
  elif sortby == 'AtoZ':
    recipe_list = Recipe.objects.all().order_by('name')
  else:
    recipe_list = Recipe.objects.all().order_by('averageRating').reverse()
    sortby = 'HighestRated'

  recipesPerPage = 10

  ret = getItemListAndPageList(recipe_list, recipesPerPage, request)
  recipes = ret[0]
  pages = ret[1]

  context = { 'recipe_list': recipes,
              'pages':pages,
              'sortby':sortby,}
  return render(request, 'recipe/recipeIndex.html',context)

def getItemListAndPageList(ls, perPage, request):
  paginator = Paginator(ls, perPage)

  page = request.GET.get('page')
  try:
    sublist = paginator.page(page)
    page = int(page)
  except PageNotAnInteger:
    # if page is not an integer, deliver first page.
    sublist = paginator.page(1)
    page = 1
  except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    sublist = paginator.page(paginator.num_pages)
    page = paginator.num_pages

  pages = None
  
  if (paginator.num_pages > 1):
    startPage = max(1,page-2)
    finishPage = min(startPage+4,paginator.num_pages)
    startPage = max(1, finishPage - 4)
    pages = range(startPage,finishPage + 1)

  return (sublist, pages)
  
def recipeDetail(request, recipe_id):
  recipe = get_object_or_404(Recipe, pk=recipe_id)
  review = None
  if request.user.is_authenticated():
    revList = recipe.review_set.filter(chef_id=request.user.id)
    if revList.count() > 0:
      review = revList[0]
  return render(request, 'recipe/recipeDetail.html', {'recipe':recipe, 'review':review})
  
def recipeReviews(request, recipe_id):
  recipe = get_object_or_404(Recipe, pk=recipe_id)
  return render(request, 'recipe/recipeReviews.html', {'recipe':recipe})

def chefIndex(request, sortby = 'Newest'):
  if sortby == 'AtoZ':
    chef_list = Chef.objects.all().order_by('username')
  else: # sortby == 'Newest'
    chef_list = Chef.objects.all().order_by('id').reverse()
    sortby = 'Newest'

  chefsPerPage = 10

  ret = getItemListAndPageList(chef_list, chefsPerPage, request)
  chefs = ret[0]
  pages = ret[1]

  context = { 'chef_list' : chefs,
              'pages' : pages,
              'sortby': sortby , }
  return render(request, 'recipe/chefIndex.html', context)

def chefDetail(request, chef_id, showrecipes = 'Originals'):
  chef = get_object_or_404(Chef, pk=chef_id)
  if showrecipes == 'Favorites':
    recipe_list = []
    fav_list = Chef_favoriteRecipes.objects.filter(chef_id=chef_id).order_by('id').reverse()
    for fav in fav_list:
      recipe_list.append(fav.recipe)
  elif showrecipes == 'Modified':
    recipe_list = chef.recipe_set.all().exclude(previousVersion__exact=None)
  else: # Originals
    recipe_list = chef.recipe_set.all().filter(previousVersion__exact=None)
    showrecipes = 'Originals'

  recipesPerPage = 5

  ret = getItemListAndPageList(recipe_list, recipesPerPage, request)
  recipes = ret[0]
  pages = ret[1]

  context = { 'chef':chef,
              'recipe_list': recipes,
              'pages':pages,
              'showrecipes':showrecipes,}

  return render(request, 'recipe/chefDetail.html', context)

''' links used now
def getPic(request, pic_name):
  api = BasicClient('VATx6OASrU4KYLaWshrxIvyyYUIl8x','xkpKJ3Wti1cXilKJYnMSqaOLvmNnwe')
  pic = api.get('/path/data/images/',pic_name)
  #img = zlib.decompress(pic.data, 16+zlib.MAX_WBITS)
  img = pic.data
  response = HttpResponse(img, content_type='image')
  return response'''

def addChef(request):
  if request.method == 'POST':
    form = forms.AddChef(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
      email = form.cleaned_data['email']
      newChef = Chef.objects.create_user(username,email,password)
      newChef.first_name = form.cleaned_data['first_name']
      newChef.last_name = form.cleaned_data['last_name']
      newChef.save()
      user = authenticate(username=username,password=password)
      # assuming authenticate works
      login(request, user)
      return HttpResponseRedirect('/chefs/'+str(newChef.id))
  else:
    form = forms.AddChef()
  return render(request, 'recipe/addChef.html', {'form':form})

@login_required(login_url='/login/')
def addToFavorites(request, recipe_id):
  #does this check in case they tried to add to favorites when logged out
  if Recipe.objects.get(id=recipe_id) not in Chef.objects.get(id=request.user.id).recipe_set.all():
    Chef_favoriteRecipes.objects.create(chef_id=request.user.id,recipe_id=recipe_id)
  return HttpResponseRedirect('/recipes/'+str(recipe_id))

@login_required(login_url='/login/')
def removeFromFavorites(request, recipe_id):
  fav = Chef_favoriteRecipes.objects.get(chef_id=request.user.id,recipe_id=recipe_id)
  fav.delete()
  nextPage = request.GET.get('next')
  return HttpResponseRedirect(nextPage)

''' need to change this to a simpler form
def editChef(request):
  if request.method == 'POST':
    form = UserChangeForm(request.POST)
    if form.is_valid():
      print form.cleaned_data
      return HttpResponseRedirect('/chefs/')#+str(newChef.id))
  else:
    form = UserChangeForm()
  return render(request, 'recipe/editChef.html', {'form':form})'''

@login_required(login_url='/login/')
def addReview(request,recipe_id):
  recipe = get_object_or_404(Recipe, pk=recipe_id)
  if request.method == 'POST':
    comment = request.POST.get('Comment')
    rating = request.POST.get('staraddStars')
    revList = recipe.review_set.filter(chef_id=request.user.id)
    if revList.count() > 0:
      review = revList[0]
      review.comment = comment
      review.rating = rating
      review.save()
    else:
      recipe.review_set.create(comment=comment,rating=rating,chef_id=request.user.id)
    return HttpResponseRedirect('/recipes/'+str(recipe_id))

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

def createLink(rpic,fileName,picName):
  rpic.setPath(fileName)
  rpic.setSmallPath(picName[0]+'_thumb.jpg')

@login_required(login_url='/login/')
def addRecipe(request):
  if request.method == 'POST':
    form = forms.AddRecipe(request.POST, request.FILES, extra=request.POST.get('inst'), ings=request.POST.get('ings'), pics=request.POST.get('pics'))
    if form.is_valid():
      recipeName = form.cleaned_data['recipe_Name']
      prepTime = form.cleaned_data['prep_Time']
      cookTime = form.cleaned_data['cook_Time']
      comments = form.cleaned_data['comments']
      
      instructions = form.cleaned_data['instructions']

      #api.post('/path/data/images/', file=(recipeName+'.'+picName[-1], picData))

      recipe = Recipe.objects.create(chef=get_object_or_404(Chef, pk=request.user.id), name=recipeName, prepTime=prepTime, cookTime=cookTime, chefComment=comments)
      ids = str(recipe.id)

      recipe.instruction_set.create(text=instructions)
      for i in range(form.cleaned_data['inst']):
        inst = request.POST.get('extra_field_'+str(i+1))
        recipe.instruction_set.create(text=inst)


      for i in range(form.cleaned_data['ings']):
        ingName = request.POST.get('extra_ings_'+str(i))
        amount = request.POST.get('amount_extra_ings_'+str(i))
        unitName = request.POST.get('unit_extra_ings_'+str(i))
        unit = UnitOfMeasure.objects.create(name=unitName)

        ingList = Ingredient.objects.filter(name=ingName)
        if ingList.count()>0:
          ingredient = ingList[0]
        else:
          ingredient = Ingredient.objects.create(name=ingName)
        RecipeIngredient.objects.create(recipe=recipe,ingredient=ingredient,amount=amount,unit=unit)

      api = BasicClient('VATx6OASrU4KYLaWshrxIvyyYUIl8x','xkpKJ3Wti1cXilKJYnMSqaOLvmNnwe')

      #make folder for pictures
      pictureFolder = '/RecipePicture/'+ids+'/'
      api.post('/path/oper/mkdir',path=pictureFolder)

      for p in request.FILES.getlist('picture'):
        picName = p.name.split(".")
        tempPictureName = "tmp."+picName[-1]
        with open(tempPictureName, 'wb+') as destination:
          for chunk in p.chunks():
            destination.write(chunk)

        destination.close()
        #im = Image.open(StringIO(file(tempPictureName,"rb").read())) 
        im = Image.open(tempPictureName)
        size = 64, 64
        im.save(picName[0]+"."+picName[-1], "JPEG", quality=30)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save("thumb.jpg", "JPEG")

        #upload picture
        fileName = recipeName+'_'+picName[0]+'.'+picName[-1]
        api.post('/path/data'+pictureFolder, file=(fileName, open(picName[0]+"."+picName[-1], 'r').read()))
        api.post('/path/data'+pictureFolder, file=(picName[0]+'_thumb.jpg', open('thumb.'+picName[-1], 'r').read()))

        #make picture object
        rpic = recipe.recipepicture_set.create()
        t = Thread(target=createLink, args=(rpic,fileName,picName))
        t.start()

        #set this pic as recipe's main pic
        recipe.mainPicture = rpic
      recipe.save()

      return HttpResponseRedirect('/recipes')
  else:
    form = forms.AddRecipe()
  ingredients = Ingredient.objects.all()

  ings = "["
  for i in ingredients:
    ings += '"'+i.name+'",'
  ings = ings[:-1]+']' 
  
  units = UnitOfMeasure.objects.all()

  return render(request, 'recipe/addRecipe.html', {'form':form, 'ingredients':ings, 'units': units})

def test(request):
  return render(request, 'recipe/test.html', {})

''' pdf's suck
def pdf(request):
  scriptPath = os.path.abspath(os.path.join(os.path.dirname(__file__),"wkhtmltopdf-i386"))
  pdfPath = os.path.abspath(os.path.join(os.path.dirname(__file__),"pdf.pdf"))
  args = [scriptPath, "--footer-center", '[page]', 'http://infinite-garden-1600.herokuapp.com/']
  args.append(pdfPath)
  os.system(" ".join(args))

  api = BasicClient('VATx6OASrU4KYLaWshrxIvyyYUIl8x','xkpKJ3Wti1cXilKJYnMSqaOLvmNnwe')
  api.post('/path/data', file=('pdf.pdf', open(pdfPath, 'r').read()))

  return HttpResponseRedirect('/')'''

