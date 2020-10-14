import random
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello_world(request):
    result = random.randint(1, 100)
    return HttpResponse(f"Hello world!!! With random int - {result}")
