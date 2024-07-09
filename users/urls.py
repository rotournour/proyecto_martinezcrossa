from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import register, update_user, user_login


urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', register, name = 'register'),
    path('update-user/', update_user)
    
    ]

