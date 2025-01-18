# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_student", views.add_student, name="add_student"),
    path("query_student", views.query_student, name="query_student"),
]