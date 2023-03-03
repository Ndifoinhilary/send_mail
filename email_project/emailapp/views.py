from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.core.mail import send_mail


def home(request):
    if request.method == "POST":
        su = request.POST['subject']
        email = request.POST['email']
        mgs = request.POST['message']
        
        
        send_mail(su,mgs,'ndifoinhilary@gmail.com',['bosoyoj200@wwgoc.com'],fail_silently=False)  
        return HttpResponse('Mail send! ') 
    return render(request,'home.html')