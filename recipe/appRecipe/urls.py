from django.conf.urls import patterns, url

from appRecipe import views

urlpatterns = patterns('',
  # ex: /recipes/
  url(r'^recipes/$', views.recipeIndex, name='recipeIndex'),
  # ex: /recipes/3/
  url(r'^recipes/(?P<recipe_id>\d+)/$', views.recipeDetail, name='recipeDetail'),
  # ex: /recipes/3/ingredients
  url(r'^recipes/(?P<recipe_id>\d+)/ingredients/$', views.recipeIngredients, name='recipeIngredients'),
)