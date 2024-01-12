from django.shortcuts import render,HttpResponse,redirect
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from django.db import models
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Contact
from .models import RegUsers
from .models import Customer


from joblib import load
decision=load('savedmodels/model.joblib')

from joblib import load
scaler1=load('savedmodels/scaler.joblib')

customer=pd.read_excel('customer.xlsx')
arrcustomer=np.asarray(customer)






# Create your views here.
@login_required(login_url='login')
def predictor(request):
    return render(request,'main.html')

def SignUpPage(request):
    if request.method=='POST':
        orgname=request.POST.get('orgname')
        branch=request.POST.get('branch')
        number=request.POST.get('number')
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pw=request.POST.get('password')
        pw1=request.POST.get('confirmpassword')
        if pw!=pw1:
            messages.error(request, "The entered passwords do not match")
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.warning(request, "Email address already exists")
            return redirect('signup')
        elif User.objects.filter(username=uname).exists():
            messages.warning(request, "Username already taken")
            return redirect('signup')
        else:
            reg=RegUsers()
            reg.cName=orgname
            reg.cBranch=branch
            reg.cNumber=number
            reg.cEmail=email
            reg.cUsername=uname
            reg.save()
            my_user=User.objects.create_user(uname,email,pw)
            my_user.save()
            messages.success(request, "User Created Successfully! Thank you for registering.")
            return redirect('login')
        
        
    return render(request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        uname2=request.POST.get('username')
        passw=request.POST.get('password')
        user=authenticate(request,username=uname2,password=passw)
        if user is not None:
            login(request,user)
            return redirect('predictor')
        else:
            messages.warning(request, "Incorrect username or password")
            return redirect('login')
    return render(request,'login.html')

def LogOut(request):
    logout(request)
    return redirect('login')




def HomePage(request):
    return render(request,'home.html')


def AboutPage(request):
    return render(request,'about.html')

def HowToUse(request):
    return render(request,'howto.html')

def Enquirys(request):
    if request.method=='POST':
        contact=Contact()
        ename=request.POST.get('ename')
        address=request.POST.get('address')
        emailadd=request.POST.get('emailadd')
        num=request.POST.get('num')
        message=request.POST.get('message')
        contact.ename=ename
        contact.address=address
        contact.emailadd=emailadd
        contact.num=num
        contact.message=message
        contact.save()
        messages.success(request, "Thank you for the enquiry. We will get back to you soon.")
        return redirect('enquiry')
    return render(request, 'enquiry.html')

def display(request):
    st=Contact.objects.filter(id=1)
    return render(request,'sample.html',{'st':st})
    


@login_required(login_url='login')
def result(request):
    
    id=request.GET['id']
    a=request.GET['seniorcitizen']
    b=request.GET['tenure']
    c=request.GET['ps']
    d=request.GET['ml']
    e=request.GET['inter']
    f=request.GET['ts']
    g=request.GET['tv']
    h=request.GET['novie']
    i=request.GET['con']
    j=request.GET['mchar']
    array=(a,b,c,d,e,f,g,h,i,j)
    input_array=np.array(array)
    input_reshaped=input_array.reshape(1,-1)
    
    
    std_data=scaler1.transform(input_reshaped)
    result=decision.predict(std_data)
    
    dist = decision.decision_function(std_data)

    if result[0]==1:
        re='has possibility to churn.'
        prob=(float(dist)/2.399)*100
        probs=round(prob,2)
        if input_array[2]=='1':
            comi='Your customer may not be satisfied by the Phone service.'
        else: 
            comi="Your customer might have got phone services at more reasonable price."
        if input_array[4]=='1':
            comii="Your customer may not be satisfied by the quality of Internet service or may have received better offers from other companies in the market."
        else: 
            comii="Your customer may have received better offers from other companies in the market."
        if input_array[5]=='0':
            comiii='Your customer may not have been receiving timely response and the desired solution from the Tech Support Team.'
        else: 
            comiii="Your customer is not well known to the Tech Suppport they can utilize."
        if input_array[6]=='1':
            comiv='Your customer may not find the TV Package satisfactory'
        else:
            comiv='Your customer may have found better alternatives for TV subscription.' 
        if input_array[7]=='1':
            comv='Your customer may want better OTT platform for movies.'     
        else:
            comv='Your customer may have found better alternatives for Movies subscription.' 
        if input_array[9]=='950':
            comvi='Your customer may not have found your services economically feasible.'  
        else: 
            comvi="Your customer might have found better value for money packages from other companies." 
        id1=int(id)  
        one_data = Customer.objects.get(id=id1)  
        
        context={'outcome':re,'value':probs,'identity':id,'c1':comi,'c2':comii,'c3':comiii,'c4':comiv,'c5':comv,'c6':comvi,'cData':one_data,}
        return render(request,'result.html',context)
         
                 
            
        
        
    else:
        re='has less churn possibility.'
        prob=(float(dist)/-5.961334)*100
        probs=round(prob,2)
        id1=int(id) 
        one_data = Customer.objects.get(id=id1)  
        return render(request,'result2.html',{'outcome':re,'identity':id,'cData':one_data,'value':probs})
        
        
        
  
    


