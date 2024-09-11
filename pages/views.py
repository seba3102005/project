from django.shortcuts import render
from .models import *
from .form import Login_form

# Create your views here.

def index(request):
    context = {'books':Book.objects.all(),
               'total':Book.objects.count(),
    }
    return render(request,'pages/index.html' ,context)

def allBooks(request):
    all_books=Book.objects.all()
    searchans=None
    ally=Book.objects.all()
    if request.method=='GET':
        if 'search' == request.GET:
            searchans = request.GET['search']
            if searchans:
                ally=ally.filter(searchans__icontains=searchans)
            
        
            # total = all_books.__contains(searchans)

            
            

    context = {'books':Book.objects.all(),'total':ally}

    return render(request,'pages/allBooks.html',context)



def categories(request):
    
    searchans=None
    ally=Book.objects.all()
    if request.method=='GET':
        if 'search' in request.GET:
            searchans = request.GET['search']
            if searchans:
                ally=ally.filter(name__icontains=searchans)
            

    context = {'total':ally}

    return render(request,'pages/categories.html',context)

def login(request):

    if request.method=='POST':
        data_form=(Login_form(request.POST))
        if data_form.is_valid():
            data_form.save()



    return render(request,'pages/login.html' ,{'lf':Login_form})

