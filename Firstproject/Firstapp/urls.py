from django.urls import path
from Firstapp import views

urlpatterns = [
    path("", views.index, name="index"),
]