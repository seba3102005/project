from django.urls import path
from . import views
urlpatterns=[
    path('fiction/',views.fiction ,name='fiction'),
    path('nonfiction/',views.nonfiction ,name='nonfiction'),
    path('science/',views.science ,name='science'),
    path('fantasy/',views.fantasy ,name='fantasy'),
    path('mystery/',views.mystery ,name='mystery'),
    path('children/',views.children ,name='children'),
    path('biographies/',views.biographies ,name='biographies'),
    path('rent/',views.rent ,name='rent'),
    path('sold/',views.sold ,name='sold'),
    path('available/',views.available ,name='available'),
]