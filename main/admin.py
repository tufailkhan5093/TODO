from django.contrib import admin
from .models import User,Post,Personal,Fav
from django.contrib.auth.models import User

# Register your models here.



@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display=['id','user','title','body']

@admin.register(Personal)
class AdminPersonal(admin.ModelAdmin):
    list_display=['firstname','lastname']




