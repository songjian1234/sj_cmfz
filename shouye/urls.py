from django.urls import path

from shouye import views

appname = 'shouye'

urlpatterns = [
    path('shouye/',views.shouye),
]