from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home/home.html"


class AboutUsPageView(TemplateView):
    template_name = "home/aboutus.html"

class SpaceJamPageView(TemplateView):
    template_name="home/spacejam.html"
