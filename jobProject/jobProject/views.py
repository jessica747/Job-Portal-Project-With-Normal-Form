from django.shortcuts import render,redirect
from jobApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


message_box={
    'signup_success':'Signup is successfully done',
    'password_warning':'password do not match',
    'signin_success' : 'signin successfully done ',
    'signin_warning' :'credential does not match '
}


def signupPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        display_name=request.POST.get('display_name')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        email_address=request.POST.get('email_address')
        user_type=request.POST.get('user_type')
        profile_picture=request.FILES.get('profile_picture')

        if password==confirm_password:
            user = Custom_user_model.objects.create_user(
                username=username,
                display_name=display_name,
                password=password,
                email=email_address,
                user_type=user_type,
                profile_picture=profile_picture,
            )
            user.save()
            if user_type == "recruiter":
                recruiter_info_model.objects.create(recuser=user)
            else:
                seeker_info_model.objects.create(seekuser=user)
            messages.success(request,message_box['signup_success'])
            return redirect('signinPage')  
        else:
            messages.warning(request,message_box['password_warning'])
            return redirect('signupPage')
    return render(request,'common/signupPage.html')


def signinPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(
            username=username,
            password=password,
        )

        if user:
            login(request,user)
            messages.success(request,message_box['signin_success'])
            return redirect('dashboard')
        else:
            messages.warning(request,message_box['signin_warning'])
    return render(request,'common/signinPage.html')


def dashboard(request):
    return render(request,'common/dashboard.html')

def logoutPage(request):
    request.user
    logout(request)
    return redirect('signinPage')