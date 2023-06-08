from django.shortcuts import render
from django.http import HttpResponse

# use HttpResponse
def members(request):
    return HttpResponse("Hello world!")
