from django.shortcuts import render

# Create your views here.
from .models import Questions,Choice

def index(request):
    return render(request,'polls/index.html')
