from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.home_page, name="home"),
    path("create/", views.create_article, name="create"),
    path("update/<int:article_id>/", views.update_article, name="update"),
    path("delete/<int:article_id>/", views.delete_article, name="delete"),
    path("detail/<int:article_id>/", views.article_page, name="detail"),
]