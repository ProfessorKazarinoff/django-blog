# pages/views.py
from django.views.generic import TemplateView

class AboutPageView(TemplateView):
    template_name = 'about.html'
