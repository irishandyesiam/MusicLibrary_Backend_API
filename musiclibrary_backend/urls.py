from django.urls import path
from  . import views

urlpatterns = [
    path('', views.musiclibrary_list)
]