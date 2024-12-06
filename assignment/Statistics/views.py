from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm


# Create your views here.

def homepage(request):
    if request.method == 'Post'