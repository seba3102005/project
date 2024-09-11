from django.urls import path
from . import views
urlpatterns=[
    path('', views.index ,name='index'),
    path('allBooks/',views.allBooks,name='allBooks'),
    path('categories/',views.categories, name='categories'),
    path('login/',views.login, name='login'),
    

]