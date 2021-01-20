from django.urls import path

from .views import AboutUsPageView, HomePageView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("About-Us", AboutUsPageView.as_view(), name="aboutus"),
]
