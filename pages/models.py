from django.db import models

# Create your models here.

class Book (models.Model):

    choice=[
        ('available','available'),
        ('sold','sold'),
        ('rent' ,'rent'),
    ]
    choice2=[('fiction','fiction'),('nonfiction','nonfiction'),('science','science'),('mystery','mystery'),('fantasy','fantasy'),("children","children"),("biographies","biographies"),]

    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7,decimal_places=2,blank=True,null=True)
    status = models.CharField(choices=choice ,max_length=50)
    rent_price = models.DecimalField(max_digits=7,decimal_places=2,blank=True ,null=True)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    category = models.CharField(max_length=50 , choices=choice2 ,null='true',blank='True')
    def __str__(self) :
        return self.name
    

class Login (models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username

