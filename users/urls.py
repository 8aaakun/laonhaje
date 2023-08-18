from django.urls import path
from .views import signup, login_view

app_name = 'users'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
]