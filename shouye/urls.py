from django.urls import path

from shouye import views

appname = 'shouye'

urlpatterns = [
    path('shouye/', views.shouye),
    path("login/", views.login_form),
    path("get_code/", views.get_code),
    path("check_user/", views.check_user),
]
