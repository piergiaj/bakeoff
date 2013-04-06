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


