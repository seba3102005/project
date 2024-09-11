from django.shortcuts import render
from .models import *
# Create your views here.
def fiction (request):
    context= {'fiction':(Book.objects).filter(category='fiction')}
    return render(request,'sidebar/fiction.html',context)
def nonfiction (request):
    context= {'nonfiction':(Book.objects).filter(category='nonfiction')}
    return render(request,'sidebar/nonfiction.html',context)

def science (request):
    context= {'science':(Book.objects).filter(category='science')}
    return render(request,'sidebar/science.html',context)

def mystery (request):
    context= {'mystery':(Book.objects).filter(category='mystery')}
    return render(request,'sidebar/mystery.html',context)

def fantasy (request):
    context= {'fantasy':(Book.objects).filter(category='fantasy')}
    return render(request,'sidebar/fantasy.html',context)

def children (request):
    context= {'children':(Book.objects).filter(category="children")}
    return render(request,'sidebar/children.html',context)

def biographies (request):
    context= {'biographies':(Book.objects).filter(category="biographies")}
    return render(request,'sidebar/biographies.html',context)


def rent(request):
    context = {'rent': (Book.objects).filter(status='rent')}
    return render(request, 'sidebar/rent.html', context)

def sold(request):
    context = {'sold': (Book.objects).filter(status='sold')}
    return render(request, 'sidebar/sold.html', context)

def available(request):
    context = {'available': (Book.objects).filter(status='available')}
    return render(request, 'sidebar/available.html', context)
