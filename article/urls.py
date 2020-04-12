from django.urls import path

from article import views

urlpatterns = [
    path("getALLArticle/", views.getALLArticle),
    path("upload/", views.upload_img),
    path("load_kind/", views.load_kind),
    path("get_all_img/", views.get_all_img),
    path("add_article/", views.add_article),
    path("edit_article/", views.edit_article),
    path("del_article/", views.del_article),
]