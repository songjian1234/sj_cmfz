from django.urls import path

import user
from user import views

urlpatterns = [
    path("query_all/",views.query_all),
    path("add_banner/",views.add_banner),
    path("data_oper/",views.data_oper),
]