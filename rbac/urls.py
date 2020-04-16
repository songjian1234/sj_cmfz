from django.urls import path

from rbac import views

urlpatterns = [
    path("login/", views.login),
    path("check_user/", views.check_user),
]