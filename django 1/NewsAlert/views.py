from django.shortcuts import render , redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .models import Holder
from .check import checkstock

def portfolio(request):
    if request.method == 'GET':
        user_email = request.COOKIES.get('user_email')
        if user_email:
            if(user_email):
                stock_info = Holder.objects.filter(gmail=user_email).first()
            else:
                stock_info = None
            return render(request, "port.html", {
            'stock_info': stock_info,
            'name': user_email
        })
    if request.method =="POST":
            act = request.POST.get("act")
            if act=='add':
                name = request.POST.get("gmail")
                a = request.POST.get("stock_name")
                b = request.POST.get("stock_value")
                if checkstock(a+".NS"):
                    hold=Holder.objects.filter(gmail=name).first()
                    if hold:
                        if not hold.st1:
                            hold.st1 = a.upper()
                        elif not hold.st2:
                            hold.st2 = a.upper()
                        elif not hold.st3:
                            hold.st3 = a.upper()
                        elif not hold.st4:
                            hold.st4 = a.upper()
                        elif not hold.st5:
                            hold.st5 = a.upper()
                        else:
                            messages.error(request, "Your Limit is fulled")
                            return redirect('/login.html')
                        # Save the updated Holder instance
                        hold.save()
                    else :
                        return HttpResponse('<h1>error</h1>')
                    # Redirect to the portfolio page or render a success message
                    return HttpResponseRedirect('/NewsAlert/port.html/')
                else :
                    return HttpResponse("<h1>Stock Symbol Is Wronge</h1>")
            elif act == 'delete':
                # Delete stock based on the hidden fields
                stock_name = request.POST.get("st1del") or request.POST.get("st2del") or request.POST.get("st3del") or request.POST.get("st4del") or request.POST.get("st5del")
                name = request.POST.get("gmaildel")
                if stock_name:
                    hold = Holder.objects.filter(gmail=name).first()
                    if hold:
                        if hold.st1 == stock_name:
                            hold.st1 = None
                        elif hold.st2 == stock_name:
                            hold.st2 = None
                        elif hold.st3 == stock_name:
                            hold.st3 = None
                        elif hold.st4 == stock_name:
                            hold.st4 = None
                        elif hold.st5 == stock_name:
                            hold.st5 = None
                        hold.save()
                    else:
                        return HttpResponse('<h1>Error: Holder not found.</h1>')
                    return HttpResponseRedirect('/NewsAlert/port.html/')
            
    return render(request,'port.html')


def backtologout(request):
    return redirect('/logout.html')
def back(request):
    return redirect('/')
def backport(request):
    return redirect('/NewsAlert/port.html/')
def backsignup(request):
    return redirect('/signup.html')

    