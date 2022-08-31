from django.urls import path
from auto_response import views

urlpatterns = [
    path('', views.app_root, name='app_root'),
]