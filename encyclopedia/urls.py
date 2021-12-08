from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("title/<str:title>/", views.title, name="title"),
    path('search/', views.search, name="search")
]
