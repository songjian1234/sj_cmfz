from django.urls import path

from app import views

urlpatterns = [
    path("first_pag/", views.first_pag),
    path("wen/", views.wen),
    path("regist/", views.regist),
    path("modify/", views.modify),
]