from django.urls import path
from .views import comment, post_create_view

app_name = 'posts' #왜필요?

urlpatterns = [
    path('<int:id>/', comment, name='comment'),
    path('create/', post_create_view, name='post-create'),
]