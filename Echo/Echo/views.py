from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, "index.html")

def aboutUs(request):
    return render(request, "about-us.html")

def blog(request):
    return render(request, "blog.html")

def blogDetails(request):
    return render(request, "blog-details.html")

def contact(request):
    return render(request, "contact.html")

def rooms(request):
    return render(request, "rooms.html")

def roomDetails(request):
    return render(request, "room-details.html")

def login_signup(request):
    return render(request, "login_signup.html")


def booking(request):
    return render(request, "booking.html")

