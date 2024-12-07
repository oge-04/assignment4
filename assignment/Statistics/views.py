from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm


# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')


def results(request):
    return render(request, 'results.html')