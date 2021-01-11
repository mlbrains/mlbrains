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



def clientsignupView(request):
    ourdata = MlClient()
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            user = User.objects.create_user(name,email,password)
            ourdata.Client_email=email
            ourdata.Client_name=name
            ourdata.user=user
            user.save()
            ourdata.save()
        except:
            notification = "error"
            context = {
                'notification':notification,
            }
            return render(request, 'clientsignup.html',context)
        
        return redirect('/login/')
        
    return render(request, 'clientsignup.html')