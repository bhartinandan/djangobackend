from django.contrib import admin
from django.urls import path
from frst_prob import views

urlpatterns = [
    path("", views.index, name="frst_prob"),
    path("show", views.show_values, name="show"),
    path("coordinates", views.find_cordinates, name="coordinates")
]
