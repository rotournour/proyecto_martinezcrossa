from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from users.models import UserProfile

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = { 'username': ('Nombre de usuario' ), 'first_name': ('Nombre:'), 'last_name' :('Apellido:'), 'password1':('Contraseña:'), 'password2': ('Confirma contraseña:')}
        
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user'] 


class UpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, label='Nombre de usuario')
    class Meta:
        model = User
        fields = ['username']
        