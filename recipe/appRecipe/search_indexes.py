from haystack import indexes
from appRecipe.models import Recipe, Chef

# name every searchable field text

class RecipeIndex(indexes.SearchIndex, indexes.Indexable):
  text = indexes.CharField(document=True, use_template=True)
  chef = indexes.CharField(model_attr='chef')
  dateCreated = indexes.DateTimeField(model_attr='dateCreated')

  def get_model(self):
    return Recipe

class ChefIndex(indexes.SearchIndex, indexes.Indexable):
  text = indexes.CharField(document=True, use_template=True)
  date_joined = indexes.DateTimeField(model_attr='date_joined')

  def get_model(self):
    return Chef