from django.shortcuts import render, redirect
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

def page_not_found(request, exception=None):
    return render(request, '404.html', status=404)

def permission_denied(request, exception=None):
    return render(request, '403.html', status=403)