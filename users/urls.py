from django.urls import path
from .views import signup, login_view
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]