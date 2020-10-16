from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User,Auction_list



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def index(request):
    listing = Auction_list.objects.all()

    return render(request, "auctions/index.html",{
        "listing" : listing
    })

def create_listing(request):

    if request.method == "POST":
        create = Auction_list()

        create.seller = request.user.username
        create.title = request.POST.get('title')
        create.description = request.POST.get('description')
        create.current_price = request.POST.get('current_price')
        if request.POST.get('image_url'):
            create.image_url = request.POST.get('image_url')
        else:
            create.image_url = "https://thumbs.dreamstime.com/b/no-image-available-icon-photo-camera-flat-vector-illustration-132483141.jpg"
        
        create.save()


    
    return render (request, "auctions/create_listing.html",{
         
        })

    '''
    else:
        return render (request, "auctions/index.html",{
        "listing" : Auction_list.objects.all()
    })
    '''