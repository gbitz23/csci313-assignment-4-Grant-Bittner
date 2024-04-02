#pylint: disable=E1101
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]