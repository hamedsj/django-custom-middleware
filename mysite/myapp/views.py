from django.shortcuts import render
from django.http import HttpResponse

def myview(request):
    return HttpResponse("Hello There =)")

def process_view_test(request):
    return HttpResponse("Hello There =)")
