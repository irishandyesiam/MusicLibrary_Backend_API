from django.urls import path
from  . import views

urlpatterns = [
    path('', views.musiclibrary_list),
    path('<int:pk>/', views.musiclibrary_detail),
]