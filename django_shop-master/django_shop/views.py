import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from django_shop.settings import BASE_DIR

# Create your views here.
def index(request):
     return render(request, 'static/index.html')
    
