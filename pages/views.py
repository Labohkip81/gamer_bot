from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


#This is a fuction-based view in django.
def home_page_view(request):
    return HttpResponse('Request received 200!')
# Create your views here.

# This is a class based view in django
#Class based views should have thir names starting with a capital letter.
class HomePage(TemplateView):
    template_name = 'home.html'

class AboutPage(TemplateView):
    template_name = 'about.html'