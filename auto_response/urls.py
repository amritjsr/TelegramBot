from django.urls import path
from auto_response import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]