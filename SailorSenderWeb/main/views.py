from django.shortcuts import render
from django.http import HttpResponse
from django.template.context import RequestContext

def main(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def email(request):
    return render(request, 'main/send.html')