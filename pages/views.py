from django.shortcuts import render
from django.http import HttpResponse



def home_page_view(request):
    return HttpResponse('Request received 200!')
# Create your views here.
