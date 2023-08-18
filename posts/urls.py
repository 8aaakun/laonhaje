from django.urls import path
from .views import comment

app_name = 'posts' #왜필요?

urlpatterns = [
    path('<int:id>/', comment, name='comment'),
]