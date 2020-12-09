"""Notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import all_fav,fav_post,Search,home,signup_form,user_login,create_post,post_detail,update_post,delete_post,logout_form,Personal_data,show_personal,delete_personal
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('signup/',signup_form,name='signup'),
    path('login/',user_login,name='login'),
    path('post/',create_post,name='createpost'),
    path('post/<int:id>/',post_detail,name='postdetail'),
    path('updatepost/<int:id>/',update_post,name='updatepost'),
    path('delete/<int:id>/',delete_post,name='delete'),
    path('logout/',logout_form,name='logout'),
    path('personal/',Personal_data,name='personal'),
    path('showpersonal/',show_personal,name='showpersonal'),
    path('deletepersonal/<int:id>/',delete_personal,name='deletepersonal'),
    path('fav/<int:id>/',fav_post,name='fav'),
    path('allfav/',all_fav,name='allfav'),
  
    path('search/',Search.as_view(),name='search'),

]
