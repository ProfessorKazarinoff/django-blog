# pages/urls.py

from django.urls import path

from .views import AboutPageView, HomePageView

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("home/", HomePageView.as_view(), name="home"),
    path("", HomePageView.as_view(), name="home"),
]
