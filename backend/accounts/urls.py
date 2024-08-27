from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    # path("signup/", views.signup, name="signup"),
    path("login/", views.user_login,name="login"),
    # path("logout/", views.logout, name="logout"),
    path("profil/", views.user_profil, name="profil"),
    path("profil/<str:username>/", views.user_profil_view, name="profil_view"),
]