from django.shortcuts import render
from .forms import UserProfileInfoForm, UserForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def register(request):
    registred=False
    if request.method =="POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.User=user.username
            print("one")
            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            registred= True
            print("two")
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form= UserForm()
        profile_form = UserProfileInfoForm


    return render(request, 'basic_app/registration.html',{'user_form':user_form,'profile_form':profile_form,'registred':registred })

def user_login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if  user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("tried login and failed")
            return HttpResponse("invalid login datails")
    else:
        return render(request, 'basic_app/login.html',{})

@login_required
def special(request):
    return HttpResponse("you are log with special")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))





def another(request):
    return render(request, 'basic_app/another.html')
