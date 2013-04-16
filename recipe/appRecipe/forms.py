from django import forms

class AddChef(forms.Form):
	name = forms.CharField(max_length=50, required=True)
	email = forms.EmailField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput)


class AddRecipe(forms.Form):
	recipe_Name = forms.CharField()
	prep_Time = forms.IntegerField()
	cook_Time = forms.IntegerField()
	comments = forms.CharField(widget=forms.Textarea)
	picture = forms.ImageField(required=False)
	instructions = forms.CharField(widget=forms.Textarea)
	inst = forms.IntegerField(widget=forms.HiddenInput())
	ings = forms.IntegerField(widget=forms.HiddenInput())
	pics = forms.IntegerField(widget=forms.HiddenInput())

	def __init__(self, *args, **kwargs):
		extra_fields = kwargs.pop('extra',0)
		extra_ings = max(kwargs.pop('ings',0),2)
		extra_pics = kwargs.pop('pics',0)

		super(AddRecipe, self).__init__(*args, **kwargs)
		self.fields['inst'].initial = extra_fields
		self.fields['ings'].initial = extra_ings
		self.fields['pics'].initial = extra_pics

		for i in range(int(extra_fields)):
			self.fields['extra_fields_{index}'.format(index=i)] = forms.CharField(required=False)

		for i in range(int(extra_ings)):
			self.fields['extra_ings_{index}'.format(index=i)] = forms.CharField(required=False)

		for i in range(int(extra_pics)):
			self.fields['id_picture_{index}'.format(index=i)] = forms.ImageField(required=False)


#class Login(forms.Form):
#	username = forms.CharField()
#	password = forms.CharField(widget=forms.PasswordInput)
