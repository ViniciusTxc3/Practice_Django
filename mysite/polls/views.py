from django.shortcuts import render
from django.http import HttpResponse

# Para chamar a view precisa mapear a URL (polls/urls.py)
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")# First view

