from django.conf.urls import patterns, url, include
from recipe import settings

from appRecipe import views

urlpatterns = patterns('',
  url(r'^$', views.home, name='home'),
  # ex: /recipes/
  url(r'^recipes/$', views.recipeIndex, name='recipeIndex'),
  url(r'^recipes/sortby/(?P<sortby>.*)$', views.recipeIndex, name='recipeIndexSorted'),
  # ex: /recipes/3/
  url(r'^recipes/(?P<recipe_id>\d+)/$', views.recipeDetail, name='recipeDetail'),
  # ex: /recipes/3/ingredients
  url(r'^recipes/(?P<recipe_id>\d+)/reviews/$', views.recipeReviews, name='recipeReviews'),
  url(r'^recipes/(?P<recipe_id>\d+)/reviews/add$', views.addReview, name='addReview'),
  url(r'^recipes/(?P<recipe_id>\d+)/favorite/$', views.addToFavorites, name='addToFavorites'),
  url(r'^recipes/(?P<recipe_id>\d+)/unfavorite/$', views.removeFromFavorites, name='removeFromFavorites'),
  url(r'^recipes/add/$', views.addRecipe, name='addRecipe'),
  url(r'^recipes/(?P<recipeID>\d+)/edit/$', views.editRecipe, name='editRecipe'),

  url(r'^chefs/$', views.chefIndex, name='chefIndex'),
  url(r'^chefs/sortby/(?P<sortby>.*)$', views.chefIndex, name='chefIndexSorted'),
  url(r'^chefs/(?P<chef_id>\d+)/$', views.chefDetail, name='chefDetail'),
  url(r'^chefs/(?P<chef_id>\d+)/show/(?P<showrecipes>.*)$', views.chefDetail, name='chefDetailShowRecipes'),
  url(r'^chefs/add/$', views.addChef, name='addChef'),
#  url(r'^chefs/edit/$', views.editChef, name='editChef'), 
  url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'recipe/login.html'}),
  url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':'/'}),

  url(r'^search/', include('haystack.urls')),


  url(r'^test/$', views.test),
  url(r'^staticfiles/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
)

'''url(r'^getPic/(?P<pic_name>(\d|\D)+)/$', views.getPic, name='getPic'),'''