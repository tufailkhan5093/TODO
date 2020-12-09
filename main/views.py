from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.views import View
from django.contrib.auth.hashers import make_password,check_password
from .models import Post,Personal,Fav
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages
from .forms import Post_Update,Post_Create,LoginForm,SignupForm
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.views import View

def home(request):

    show_post=Post.objects.filter(user=request.user).order_by('-time')
    
    return render(request,'home.html',{'posts':show_post,'homee':'active'})


def post_detail(request,id):
    user=request.user
    if user:
  
        p=Post.objects.get(pk=id)
        
        is_fav=False
        if p.fav.filter(id=request.user.id).exists():
            is_fav=True
        print('present in fav')
    else:
        return redirect('login')
    
    return render(request,'postdetail.html',{'pi':p,'is_fav':is_fav})

def update_post(request,id):
    if request.method=='POST':
        pi=Post.objects.get(pk=id)
        fm=Post_Update(request.POST,instance=pi)
        if fm.is_valid():
            
            pi.save()
            messages.success(request,'Update Successfully ')
            
            return redirect('home')
                
    else:
        pi=Post.objects.get(pk=id)
        fm=Post_Update(instance=pi)
        
    return render(request,'updatepost.html',{'fm':fm})

def delete_post(request,id):
    
    pi=Post.objects.get(pk=id)
    pi.delete()
    messages.success(request,'Post Deleted Successfully')
    return redirect('home')

def logout_form(request):
    
    logout(request)
    messages.success(request,'Logout ! ')
    return redirect('login')


def create_post(request):
    user=request.user
    if user:
        
        if request.method=='POST':
            user=request.user
            title=request.POST.get('title')
            body=request.POST.get('body')
            print(body)
            print(title)
            post=Post(user=request.user,title=title,body=body)
            post.save()
            messages.success(request,'Note Created Successfully ')
            return redirect('home')
    
    else:
        return redirect('login')
        
    return render(request,'createpost.html',{'createpost':'active'})

def Personal_data(request):
    user=request.user
    if user:
        if request.method=='POST':
       
            postData=request.POST
            firstname=postData.get('firstname')
            lastname=postData.get('lastname')
            phone=postData.get('phone')
            email=postData.get('email')
            address=postData.get('address')
            state=postData.get('state')
            country=postData.get('country')
            dob=postData.get('dob')
            nickname=postData.get('nickname')
            qualification=postData.get('qualification')
            fathername=postData.get('fathername')
            postal=postData.get('postalcode')

            personal=Personal(userr=request.user,
                                firstname=firstname,
                                lastname=lastname,
                                phone=phone,
                                email=email,
                                address=address,
                                state=state,
                                country=country,
                                dob=dob,
                                nickname=nickname,
                                qualification=qualification,
                                fathername=fathername,
                                postal=postal)
            personal.save()
            messages.success(request,'Personal Data Saved ')
            return redirect('showpersonal')
           
        else:
            return render(request,'personaldata.html',{'addpersonal':'active'})
    else:
        return redirect('login')


def show_personal(request):
    if request.user.is_authenticated:
        pi=Personal.objects.filter(userr=request.user)
    else:
        return redirect('login')
    
    return render(request,'showpersonal.html',{'pi':pi,'show':'active'})
   


    
def signup_form(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=SignupForm(request.POST)
            
            if form.is_valid():
                messages.success(request,'Congratulation ,Successfully Signup ')
                user=form.save()
                
                
                return redirect('login')
        else:
            form=SignupForm()
        return render(request,'signup.html',{'form':form,'homee':'active'})
    else:

        return redirect('home')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                obj=authenticate(username=uname,password=upass)
                if obj is not None:
                    login(request,obj)
                    messages.success(request,'Successfully Login ! ')
                    return redirect('home')
                    
        else:
            form=LoginForm()
        return render(request,'login.html',{'form':form,'homee':'active'})
    else:
        return redirect('home')


def delete_personal(request,id):
    
    p=Personal.objects.get(pk=id)
    p.delete()
    messages.success(request,'Personal Info Successfully Deleted')
    return redirect('home')


    
    

class Search(ListView):
    model=Post
    template_name="search.html"
    paginate_by=5

    def get_queryset(self):
        title=self.request.GET.get("title","")
        print(title)
        queryset=Post.objects.filter(title__icontains=title)
        print(queryset)
        return queryset

def fav_post(request,id):
    p=Post.objects.get(id=id)
    if p.fav.filter(id=request.user.id).exists():
        p.fav.remove(request.user)
    else:
        p.fav.add(request.user)
    return redirect('home')

def all_fav(request):
    user=request.user
    fav_list=user.fav.all()
    print(fav_list)

    return render(request,'fav.html',{'fav_list':fav_list,'liked':'active'})
   