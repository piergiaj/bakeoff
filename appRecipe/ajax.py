from dajaxice.decorators import dajaxice_register
from appRecipe.models import RecipePicture

@dajaxice_register
def deletePic(request,id):
	RecipePicture.objects.get(id=id).delete()