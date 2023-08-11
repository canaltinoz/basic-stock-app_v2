from django import forms
from .models import CustomUser,Flavour
from django.contrib.auth.forms import AuthenticationForm

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')
        


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False)

class AddFlavourForm(forms.ModelForm):
    class Meta:
        model = Flavour
        fields = ('title', 'genre', 'quantity')

class FlavourTransactionForm(forms.Form):
    action = forms.ChoiceField(choices=[('increase', 'Increase'), ('decrease', 'Decrease')])
    flavour = forms.ModelChoiceField(queryset=Flavour.objects.all())
    quantity = forms.IntegerField(min_value=1)