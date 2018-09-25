from django.shortcuts import render
from django.http import request, HttpResponse
import base64
from .models import Faq
from .forms import RegistrationForm, LoginForm, ResetPasswordForm

SECRET_KEY = "n)yvs4u2q8p=4nck(5^=ku8il&3-6sz#u@lpf0#^q$3lc#s7h5"

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def forgot(request):
    return render(request, "reset_password.html")

def faq(request):
    context = {
        'faq': Faq.objects.all()
    }
    return render(request, "faq.html", context)

def terms(request):
    return render(request, "terms.html")

def privacy(request):
    return render(request, "privacy.html")

def register(request):
    if request.method == "POST":
        pass
    else:
        registration_form = RegistrationForm()
    context = {
        'form': registration_form
    }
    return render(request, "register.html", context)

def forgot(request):
    if request.method == "POST":
        pass
    else:
        reset_password = ResetPasswordForm()
    context = {
        'form': reset_password
    }
    return render(request, "reset_password.html", context)

def login(request):
    if request.method == "POST":
        pass
    else:
        login_form = LoginForm()
        context = {
            'form': login_form
        }
    return render(request, "login.html", context)

def encode(string, key=SECRET_KEY):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return base64.urlsafe_b64encode(encoded_string)

def decode(string, key=SECRET_KEY):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) - ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return base64.urlsafe_b64encode(encoded_string)
