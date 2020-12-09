from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime

# Create your models here.


class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=50)
    body=models.TextField(max_length=500)
    time=models.DateTimeField(auto_now_add=True)
    fav=models.ManyToManyField(User,related_name='fav',blank=True)

    




class Personal(models.Model):
    userr=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    fathername=models.CharField(max_length=50)
    postal=models.CharField(max_length=50)
    dob=models.CharField(max_length=50)
    nickname=models.CharField(max_length=50)
    qualification=models.CharField(max_length=50)


class Fav(models.Model):
    postss=models.ManyToManyField(Post,related_name='favpost')

    @classmethod
    def addfav(cls,post):
        obj,create=cls.objects.get_or_create()
        obj.postss.add(post)

    

  
    

