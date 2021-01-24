from django.urls import path

from .views import AboutUsPageView, HomePageView
from .views import SpaceJamPageView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("About-Us", AboutUsPageView.as_view(), name="aboutus"),
    path("SpaceJam", SpaceJamPageView.as_view(), name="spacejam")
]
