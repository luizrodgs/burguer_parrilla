from clients.models import Client
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect, render


def index(request):
    return render (request, 'index.html')

def client_id(request):
    return render (request, 'index.html')

def search(request):
    return render (request, 'index.html')

def create_client(request):
    return render (request, 'index.html')

def delete_client(request):
    return render (request, 'index.html')

def edit_client(request):
    return render (request, 'index.html')

def update_client(request):
    return render (request, 'index.html')