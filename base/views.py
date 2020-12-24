from django.shortcuts import render, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect, reverse
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


# Create your views here.

def signupView(request):
    ourdata = MlUser()
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            user = User.objects.create_user(name,email,password)
            ourdata.email=email
            ourdata.name=name
            ourdata.user=user
            user.save()
            ourdata.save()
        except:
            notification = "error"
            context = {
                'notification':notification,
            }
            return render(request, 'signup.html',context)
        
        return redirect('/login/')
        
    return render(request, 'signup.html')

def loginView(request):
    if request.method=='POST':
        #print(request.POST)
        email1 = request.POST.get('email')
        password1 = request.POST.get('password')
        user = authenticate(request, username=email1, password=password1)
        print(user)
        try:
            obj = MlUser.objects.get(email=email1)
        except:
            obj = None
    
        if user:
            if user.is_authenticated:
                if user.is_active:
                    login(request, user)
                    if request.GET.get('next', None):
                        return HttpResponseRedirect(request.GET['next'])
                    return HttpResponseRedirect(reverse('landingpage'))
                    notification=None
                    context = {
                        'notification':notification,
                    }
                    return render(request, 'homepage.html', context)
            else:
                user=None
                return render(request, 'login.html')
    
    return render(request, 'login.html')

def homepageView(request):
    """ if User:
        print(User.username, "userrrrr")
    else:
        print("no user") """
    emailname = request.POST.get('name')
    emailemail = request.POST.get('email')
    emailphone = request.POST.get('phone')
    emailwebsite = request.POST.get('website')
    emailsubject = request.POST.get('subject')
    emailmess = request.POST.get('message')
    print(emailemail)
    
    if emailemail:
        email=EmailMessage(
            emailsubject,
            "Email from - "+" "+str(emailemail)+",\n"+ "Message - "+ str(emailmess) +", \n"+ "Phone - "+ 
            str(emailphone)+", \n"+"Website - "+ str(emailwebsite),
            emailemail,
            [settings.EMAIL_HOST_USER],
            #fail_silently=False,
        ) 

        email.send()
        return redirect('/')
    
    return render(request, 'homepage.html')

def logoutView(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def landingpage(request):
    labels = MlUser.objects.get(user = request.user)
    projectdetails = Projectsdetail.objects.all()
    if int(labels.labels_selected) == 0:
        percentage = 0
        accuracy = 0
    else:
        percentage = int(int(labels.labels_done)/int(labels.labels_selected) * 100)
        accuracy = int(int(labels.labels_correct)/int(labels.labels_done) * 100)

    context = {
        'number':percentage,
        'projectdetails':projectdetails,
        'accuracy':accuracy
    }
    return render(request, 'landingpage.html', context)