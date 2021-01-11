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
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from Mlclient.models import *


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
            obj = MlUser.objects.get(user=user)
        except:
            obj = None
        
        try:
            obr = MlClient.objects.filter(user=user)
        except:
            obr = None

        print(obr)
    
        if obj:
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
        if obr:
            if user:
                if user.is_authenticated:
                    if user.is_active:
                        login(request, user)
                        if request.GET.get('next', None):
                            return HttpResponseRedirect(request.GET['next'])
                        return HttpResponseRedirect(reverse('dashboard'))
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
    show_project = list()
    for i in projectdetails:
        try:
            qwe = Projectsdetail.objects.get(project_ID=i)
            zxc = Elements.objects.filter(project_ID=qwe)
        except:
            zxc = None
        
        if zxc:
            show_project.append(i)
        else:
            show_project = show_project

    """ show_project = list()
    for i in projectdetails:
        if i.Total_elements>0:
            show_project.append(i)
        else:
            show_project = show_project
 """
    
    if int(labels.labels_selected) == 0:
        percentage = 0
        accuracy = 0
    else:
        percentage = int(int(labels.labels_done)/int(labels.labels_selected) * 100)
        accuracy = int(int(labels.labels_correct)/int(labels.labels_done) * 100)

    """ testingdata = pd.read_csv(r"D:\mlbrains\mlbrains\salesrecord.csv", names=['products'])
    #print(testingdata.product)
    data = list()
    data = testingdata.products
    asd = Projectsdetail.objects.get(project_ID = "Project 2")
    x = 0
    for i in data:
        Elements.objects.create(project_ID = asd, element_ID = str(asd)+"."+str(x))
        x +=1 """
    

    context = {
        'number':percentage,
        'projectdetails':show_project,
        'accuracy':accuracy
    }
    return render(request, 'landingpage.html', context)

def profileView(request):
    return render(request, 'profile.html')


def testing(request):
    allprojects = Projectsdetail.objects.all()
    if request.method == "POST":
        project_selected = request.POST.get('choices')
        images = request.FILES.getlist('images')
        asd = Projectsdetail.objects.get(project_ID = project_selected)
        if asd.Total_elements>0:
            count=asd.Total_elements
        else:
            count = 1
        for i in images:
            imagesdata = Elements(project_ID=asd, element_ID = str(asd)+"."+str(count), filename = i)
            imagesdata.save()
            count += 1
            asd.Total_elements=count
            asd.save()

    context = {
        'allprojects':allprojects,
    }
    return render(request, 'testing.html', context)

def dashboardView(request):
    allprojects = Projectsdetail.objects.all()
    if request.method == "POST":
        project_selected = request.POST.get('choices')
        images = request.FILES.getlist('images')
        asd = Projectsdetail.objects.get(project_ID = project_selected)
        if asd.Total_elements>0:
            count=asd.Total_elements
        else:
            count = 1
        for i in images:
            imagesdata = Elements(project_ID=asd, element_ID = str(asd)+"."+str(count), filename = i)
            imagesdata.save()
            count += 1
            asd.Total_elements=count
            asd.save()

    context = {
        'allprojects':allprojects,
    }
    return render(request, 'dashboard.html', context)