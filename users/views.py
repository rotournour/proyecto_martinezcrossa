from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from users.forms import UpdateForm
from users.models import UserProfile

def user_login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form':form
        }
        return render(request, 'users/login.html', context=context)
    
    elif request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                context = {
                    'message':f'Bienvenido/a a Martinez Crossa {username}.'
                }
                return render(request, 'users/login.html', context=context)

        form = AuthenticationForm()
        context ={
            'form':form,
            'errors':'Tu usuario y/o contraseña son incorrectos. Vuelve a introducirlos'
        }
        return render(request, 'users/login.html', context=context)
    
    
@login_required
def update_user(request):
    user = request.user
    if request.method == 'GET':
        form = UpdateForm(initial = {
            'username':user.username,
        })
        context ={
            'form':form
        }
        return render(request, 'users/update_user.html', context=context)

    elif request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data.get('username')
            user.save()
            
            context ={
            'message': 'Gracias por actualizar tu usuario!'
                }
            return render(request, 'users/update_user.html', context=context)
        
        context = {
            'errors':form.errors,
            'form':UpdateForm()
        }
        return render(request, 'users/update_user.html', context=context)
    