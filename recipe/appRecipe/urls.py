from django.conf.urls import patterns, url

from appRecipe import views

urlpatterns = patterns('',
  url(r'^$', views.home, name='home'),
  # ex: /recipes/
  url(r'^recipes/$', views.recipeIndex, name='recipeIndex'),
  # ex: /recipes/3/
  url(r'^recipes/(?P<recipe_id>\d+)/$', views.recipeDetail, name='recipeDetail'),
  # ex: /recipes/3/ingredients
  url(r'^recipes/(?P<recipe_id>\d+)/ingredients/$', views.recipeIngredients, name='recipeIngredients'),

  url(r'^chefs/$', views.chefIndex, name='chefIndex'),
  url(r'^chefs/(?P<chef_id>\d+)/$', views.chefDetail, name='chefDetail'),
)