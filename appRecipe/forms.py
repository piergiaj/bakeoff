from django import forms
from django.contrib.auth.forms import UserCreationForm

class AddChef(UserCreationForm):
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	chef_picture = forms.ImageField(required=False)


class AddRecipe(forms.Form):
	recipe_Name = forms.CharField()
	prep_Time = forms.IntegerField()
	cook_Time = forms.IntegerField()
	comments = forms.CharField(widget=forms.Textarea)
	picture = forms.ImageField(required=False)
	instructions = forms.CharField(widget=forms.Textarea)
	inst = forms.IntegerField(widget=forms.HiddenInput())
	ings = forms.IntegerField(widget=forms.HiddenInput())
	pics = forms.IntegerField(widget=forms.HiddenInput(), required=False)

	def __init__(self, *args, **kwargs):
		extra_fields = kwargs.pop('extra',0)
		extra_ings = max(kwargs.pop('ings',0),1)
		extra_pics = kwargs.pop('pics',0)

		super(AddRecipe, self).__init__(*args, **kwargs)
		self.instrs = []
		self.fields['inst'].initial = extra_fields
		self.fields['ings'].initial = extra_ings
		self.fields['pics'].initial = extra_pics

		for i in range(int(extra_fields)):
			self.fields['extra_fields_{index}'.format(index=i)] = forms.CharField(required=False, widget=forms.Textarea)

		for i in range(int(extra_ings)):
			self.fields['extra_ings_{index}'.format(index=i)] = forms.CharField(required=False)

		for i in range(int(extra_pics)):
			self.fields['id_picture_{index}'.format(index=i)] = forms.ImageField(required=False)


#class Login(forms.Form):
#	username = forms.CharField()
#	password = forms.CharField(widget=forms.PasswordInput)
