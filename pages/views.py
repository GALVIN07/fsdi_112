from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"

class AboutMeView(TemplateView):
    template_name = "about_me.html"



# Create your views here.
