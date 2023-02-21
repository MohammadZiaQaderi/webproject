#me zia has created this file
#from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

from django.conf import settings
from .models import Database

def index(request):
    return render(request,"index.html")
def index3(request):
    user = Database.objects.all()
    return render(request,"index3.html",{'user':user})
def  showMessage(request):
     user = Database.objects.all()
     if take_input(request)==True:
        return render(request,"index2.html",{'user':user})
     else:
         return render(request,"index.html",{'name':'Something went wrong...'})
def take_input(request):
     names=request.GET.get('inputName','defaultName')
     dobs=request.GET.get('inputDateOfBirth','defaultdop')
     phones=request.GET.get('inputPhone')
     mails=request.GET.get('inputEmail')
     inputs=Database(Name=names,DateOfBirth=dobs,PhoneNumber=phones,EmailID=mails)
     try:
       inputs.save()
       import smtplib
       servers=smtplib.SMTP('smtp.gmail.com',587)
       servers.starttls()
       servers.login('mohammad.mobicloud@gmail.com','ambuqljucvknpxqk')
       servers.sendmail('mohammad.mobicloud@gmail.com',mails,'hi! '+names+' thank you for registering with us!.')
       print("mail sent...")
       print("hi from try block...")
       return True
     except:
         return False