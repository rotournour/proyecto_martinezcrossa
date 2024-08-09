from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import update_user, user_login
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('update-user/', update_user)
    
    ]

