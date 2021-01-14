from django.urls import path

from .views import HomePageView
from .views import AboutUsPageView

urlpatterns =   [path("", HomePageView.as_view(), name="home"),
                path("About-Us", AboutUsPageView.as_view(), name="aboutus")]
