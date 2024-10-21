from django.shortcuts import render
from django.contrib.auth.views import LoginView
# Create your views here.
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

   
class CustomLoginView(LoginView):
    template_name = 'login.html'
