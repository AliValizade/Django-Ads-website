from django.shortcuts import render
from django.views.generic import *

from .models import *

class HomePageView(TemplateView):
    template_name = 'home.html'

class AdListView(ListView):
    model = Ad
    template_name = 'ads/ad_list.html'
    context_object_name = 'ads'


class AdDetailView(DeleteView):
    model = Ad
    template_name = 'ads/ad_detail.html'
    context_object_name = 'ad'
