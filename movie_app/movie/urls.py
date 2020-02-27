from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('delete/<search_title>/', views.delete_movie, name="delete-movie")
]
