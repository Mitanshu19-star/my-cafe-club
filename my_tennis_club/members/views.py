from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from .models import Member


# Create your views here.
def members(request):
    template = loader.get_template("navbar.html")
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template("about.html")
    return HttpResponse(template.render())


def order(request):
    template = loader.get_template("order.html")
    return HttpResponse(template.render())


def menu(request):
    template = loader.get_template("menu.html")
    return HttpResponse(template.render())

def profile(request):
    template = loader.get_template("profile.html")
    return HttpResponse(template.render())


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def navbar(request):
    template = loader.get_template("navbar.html")
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template("contact.html")
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())

# post GET method both on capital
# GET login me 
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Find member matching the credentials
        user = Member.objects.filter(email=email, password=password).first()

        if user is not None:
            # Successfully logged in
            messages.success(request, "Logged in successfully!")
            return redirect('navbar')
        else:
            messages.error(request, "Invalid email or password.")
            return render(request, 'login.html')

    return render(request, 'login.html')     

# POST GET method
def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        Member.objects.create(
            name=name,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully!")
        return redirect('login')

    return render(request, 'register.html')
