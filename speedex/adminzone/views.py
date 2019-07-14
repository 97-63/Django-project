from django.shortcuts import render,redirect
from datetime import date
from .models import Notification,City,Packet,Quali
from .refgen import getref
from generalzone.models import Career,Complain
# Create your views here.
def adminhome(request):
    try:
        if request.session["username"]:
           notification=Notification.objects.all()
           return render(request,'adminhome.html',{'notification':notification})
    except KeyError:
        return render(request, 'login.html')
def logout(request):
    del request.session["username"]
    return render(request,'logout.html')

def careermanagement(request):
    try:
        if request.session["username"]:
            car=Career.objects.all()
            return render(request,'careermanagement.html',{'car':car})
    except KeyError:
        return render(request, 'login.html')


def addnotification(request):
    notificationmsg=request.POST['notificationmsg']
    today=date.today()
    posteddate=today.strftime('%d/%m/%Y')
    n=Notification(notificationmsg=notificationmsg,posteddate=posteddate)
    n.save()
    return redirect('adminhome')


def delete(request,id):
    en=Notification.objects.get(id=id)# now select object matching the id of same id as given in parameter
    en.delete()
    return redirect('adminhome')# redirect is used when you have to go in another function here you will go to adminhome function.

def cities(request):
    cityname=request.POST['cityname']# here cityname should be same as cityname (i.e the field name as given in form as your request.post is fetching cityname from action={% url cities %} and in that cities cityname is the name of field.)
    n=City(cityname=cityname)
    n.save()
    return redirect('city')

def delete1(request,id):
    en=City.objects.get(id=id)# get is used when you want to get some field info. from a visible html page in tjhis case you are trying to fetch data from city.html
    en.delete()
    return redirect('city')

def city(request):
    try:
        if request.session["username"]:
           x=City.objects.all()
           return render(request,'city.html',{'x':x})
    except KeyError:
        return render(request, 'login.html')

def packet(request):
    try:
        if request.session["username"]:
            cities=City.objects.all()
            refno=getref()
            return render(request,'packet.html',{'cities':cities,'refno':refno})#HERE refno might be a simple variable but here you can pass it through making a dictionery only.
    except KeyError:
        return render(request, 'login.html')

def packupdel(request):
    try:
        if request.session["username"]:
             p=Packet.objects.all()
             return render(request,'packupdel.html',{'p':p})
    except KeyError:
        return render(request, 'login.html')

def delete3(request,refno):
    en=Packet.objects.get(refno=refno)# get is used when you want to get some field info. from a visible html page in tjhis case you are trying to fetch data from city.html
    en.delete()
    return redirect('packupdel')

def delete4(request,id):
    en = Career.objects.get(id=id)  # now select object matching the id of same id as given in parameter
    en.delete()
    return redirect('careermanagement')

def calling(request):
    refno = request.POST['refno']
    sendername = request.POST['sendername']
    senderaddress = request.POST['senderaddress']
    sendermobno = request.POST['sendermobno']
    receivername = request.POST['receivername']
    receiveraddress = request.POST['receiveraddress']
    receivermobno = request.POST['receivermobno']
    source = request.POST['source']  # senders city name
    mid = request.POST['mid']  # intermediates cities
    destination = request.POST['destination']  # recivers city name
    weight = request.POST['weight']  # packet weight its charfield so that grams kg is also accomodated
    charge = request.POST['charge']
    today = date.today()
    posteddate = today.strftime('%d/%m/%Y')
    status = request.POST['status']
    n=Packet(refno=refno,sendername=sendername,senderaddress=senderaddress,sendermobno=sendermobno,receivername=receivername,receiveraddress=receiveraddress,receivermobno=receivermobno,source=source,mid=mid,destination=destination,weight=weight,charge=charge,posteddate=posteddate,status=status)
    n.save()
    return redirect('packet')

def quali(request):
    try:
        if request.session["username"]:
            qualify=Quali.objects.all()
            return render(request,'qualification.html',{'qualify':qualify})
    except KeyError:
        return render(request, 'login.html')

def seequalification(request):
    applicantquali=request.POST['applicantquali']
    ob=Quali(applicantquali=applicantquali)
    ob.save()
    return redirect('qualification')

def qualification(request):
    try:
        if request.session["username"]:
            return render(request,'qualification.html')
    except KeyError:
        return render(request, 'login.html')


def delete2(request,id):
    en=Quali.objects.get(id=id)
    en.delete()
    return redirect('quali')

def update(request,refno):
    try:
        if request.session["username"]:
            en=Packet.objects.get(refno=refno)
            return render(request, 'update.html', {'en': en})
    except KeyError:
        return render(request, 'login.html')

def upack(request):
    refno = request.POST['refno']
    sendername = request.POST['sendername']
    senderaddress = request.POST['senderaddress']
    sendermobno = request.POST['sendermobno']
    receivername = request.POST['receivername']
    receiveraddress = request.POST['receiveraddress']
    receivermobno = request.POST['receivermobno']
    source = request.POST['source']  # senders city name
    mid = request.POST['mid']  # intermediates cities
    destination = request.POST['destination']  # recivers city name
    weight = request.POST['weight']  # packet weight its charfield so that grams kg is also accomodated
    charge = request.POST['charge']
    today = date.today()
    posteddate = today.strftime('%d/%m/%Y')
    status = request.POST['status']
    o = Packet(refno=refno, sendername=sendername, senderaddress=senderaddress, sendermobno=sendermobno,receivername=receivername, receiveraddress=receiveraddress, receivermobno=receivermobno, source=source,mid=mid, destination=destination, weight=weight, charge=charge, posteddate=posteddate, status=status)
    o.save()
    return redirect('packupdel')

def managecomplain(request):
    try:
        if request.session["username"]:
            p=Complain.objects.all()
            return render(request, 'managecomplain.html', {'p': p})
    except KeyError:
        return render(request, 'login.html')

def delete5(request,contactno):
    en=Complain.objects.get(contactno=contactno)
    en.delete()
    return redirect('managecomplain')