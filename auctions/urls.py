from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("listing", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("category", views.category, name="category"),
    path("category_listing/<str:type>", views.category_listing, name="type"),
]
