from django.shortcuts import render,redirect
from django.http import HttpResponse ,HttpResponseRedirect
from django.contrib import messages
from NewsAlert.models import Holder
def isgmail(gmail):
    return (gmail.lower().endswith('@gmail.com') or gmail.lower().endswith('@email.com'))
def index(request):
    user_email = request.COOKIES.get('user_email')
    if user_email:
        return render(request,"index.html",{'email':user_email})
    else:
        return render(request,"index.html")
# user_email = request.COOKIES.get('user_email')
def signup(request):
    if(request.method=="POST"):
        g=request.POST.get("gmail")
        p=request.POST.get("password")
        if isgmail(g):
            if not(Holder.objects.filter(gmail=g).exists()):
                Holder.objects.create(
                gmail=g,
                paswrd=p
                )
                url='/NewsAlert/port.html'
                response=HttpResponseRedirect(url)
                response.set_cookie('user_email', g, max_age=3600)
                return response
            else :
                messages.error(request, "User Already Exists")
                return redirect('/signup.html')
        else :
            messages.error(request,"Enter valid gmail")
            return redirect('/signup.html')
    return render(request,"signup.html")
def login(request):
    if(request.method=="POST"):
        g=request.POST.get("gmail")
        p=request.POST.get("password")
        if (Holder.objects.filter(gmail=g).exists()):
            hold=Holder.objects.filter(gmail=g).first()
            if(hold.paswrd==p):
                url='/NewsAlert/port.html'
                response=HttpResponseRedirect(url)
                response.set_cookie('user_email', g, max_age=3600)
                return response
            else:
                messages.error(request, "Password Not Matched")
                return redirect('/login.html')
        else:
            messages.error(request, "Account Not Found")
            return redirect('/login.html')
    return render(request,"login.html")

def logout(request):
    response = redirect('index.html')
    response.delete_cookie('user_email')
    return response
