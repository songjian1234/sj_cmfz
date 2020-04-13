from django.urls import path

from album import views

urlpatterns = [
    path("getAllAlbum/", views.getAllAlbum),
    path("getChapterByAlbumId/", views.getChapterByAlbumId),
    path("add_album/", views.add_album),
    path("editAlbum/", views.editAlbum),
    path("add_chapter/", views.add_chapter),
    path("editAlbum_1/", views.editAlbum_1),
]