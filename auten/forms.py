from django import forms
class LoginForm(forms.Form):
	usuario =forms.CharField(widget=forms.TextInput())
	password=forms.CharField(widget=forms.PasswordInput(render_value=False))