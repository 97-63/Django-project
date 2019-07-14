from django.shortcuts import render,redirect
from . models import Complain,Career,LoginInfo
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ObjectDoesNotExist
from adminzone.models import Notification,Packet,Quali#you can import models of another app.

# Create your views here.
def index(request):
    notification=Notification.objects.all()
    return render(request,'index.html',{'notification':notification})

def about(request):
    return render(request,'about.html')

def login(request):
    return render(request, 'login.html')

def care(request):
    c = Quali.objects.all()
    return render(request, 'career.html',{'c':c})
def career(request):
    if request.method=='POST' and request.FILES['cv']:
        name=request.POST['name']
        gender=request.POST['gender']
        qualification=request.POST['qualification']
        experience=request.POST['experience']
        address=request.POST['address']
        contactno=request.POST['contactno']
        emailaddress=request.POST['emailaddress']

        myfile=request.FILES['cv']
        cv=myfile.name
        cr=Career(name=name,gender=gender,qualification=qualification,experience=experience,address=address,contactno=contactno,emailaddress=emailaddress,cv=cv)
        cr.save()
        fs=FileSystemStorage()
        fs.save(myfile.name,myfile)

        return render(request, 'career.html',{'message':'You are sucessfully applied for jobs'},{'c':c})
    return render(request,'career.html')

def complain(request):
    return render(request, 'complain.html')

def newcomplain(request):
    name=request.POST['name']
    gender=request.POST['gender']
    subject=request.POST['subject']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    complaintext=request.POST['complaintext']
    c=Complain(name=name,gender=gender,subject=subject,contactno=contactno,emailaddress=emailaddress,complaintext=complaintext)
    c.save()
    return redirect('index')

def validateuser(request):
    username=request.POST['username']
    password=request.POST['password']
    try:
        user=LoginInfo.objects.get(username=username,password=password)#user will get true or false as a result
        if user is not None:
            request.session["username"]=username#here username is a variable key to be more presice its a key of session whose value is going to be assigned now.in place of right side username you can write any other name as well.
            return render(request,'adminhome.html')
    except ObjectDoesNotExist:
        return redirect(login)
    return render(request,'index.html')

def consign(request):
    try:
        reno=request.POST['refno']#taking reference no from index page
        r=Packet.objects.get(refno=reno)
        if r is not None:
           return render(request,'index.html',{'r':r})
    except ObjectDoesNotExist:
        return render(request,'index.html',{'msg':'reference no is not valid'})



