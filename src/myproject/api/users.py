from django.http import HttpResponseRedirect
from django.shortcuts import render
from myproject.hospital.users import Patient
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from myproject.hospital.apikey import ApiKey


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        puser = Patient(user=user)
        puser.save()
        return HttpResponseRedirect("/api/login")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            puser = Patient.objects.get(user=user)
            api_key = ApiKey.objects.get(user=puser)
            request.session['username'] = user.username
            request.session['api_key'] = api_key.api_key
            return HttpResponseRedirect("/home")
        else:
            return render(request, "login.html", context={'error_message':'Wrong username or password'})


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/api/login')

