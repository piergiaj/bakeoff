from django.conf.urls import patterns, url, include

from appRecipe import views

urlpatterns = patterns('',
  url(r'^$', views.home, name='home'),
  # ex: /recipes/
  url(r'^recipes/$', views.recipeIndex, name='recipeIndex'),
  # ex: /recipes/3/
  url(r'^recipes/(?P<recipe_id>\d+)/$', views.recipeDetail, name='recipeDetail'),
  # ex: /recipes/3/ingredients
  url(r'^recipes/(?P<recipe_id>\d+)/ingredients/$', views.recipeIngredients, name='recipeIngredients'),
  url(r'^recipes/add/$', views.addRecipe, name='addRecipe'),

  url(r'^chefs/$', views.chefIndex, name='chefIndex'),
  url(r'^chefs/(?P<chef_id>\d+)/$', views.chefDetail, name='chefDetail'),
  url(r'^chefs/add/$', views.addChef, name='addChef'), 
  url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'recipe/login.html'}),
  url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':'/'}),

  url(r'^search/', include('haystack.urls')),

  url(r'^getPic/(?P<pic_name>(\d|\D)+)/$', views.getPic, name='getPic'),

  url(r'^test/$', views.test),
)