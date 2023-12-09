from django.shortcuts import render
from datetime import datetime, timedelta
from pytz import timezone
from django.db import IntegrityError
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from .models import *
# Create your views here.
def index(request):
    products = Product.objects.all()
    now = datetime.now(timezone('Asia/Ho_Chi_Minh'))
    target_datetime = datetime(2023, 12, 5, 20, 0, 0, tzinfo=timezone('Asia/Ho_Chi_Minh'))
    if target_datetime > now:
        return render(request, "interface/countdown.html")
    else:
        return render(request,  "interface/commerce.html", {
            "products": products,
        })
def blog(request):
    blogs = Blog.objects.all()
    return render(request, "interface/blog.html", {
      "blogs": blogs,
    })

def countdown(request):
    return render(request, "interface/countdown.html")

def blog_view(request, blog_id):
    try: 
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        return HttpResponse("Page not found")
    return render(request, "interface/blog_view.html", {
        "blog": blog,
    })

@login_required
def product_view(request, product_id):
    try: 
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return HttpResponse("Page not found")
    added = product.shoppers.filter(pk=request.user.pk).exists()
    if request.method == "POST":
        if added:
            product.shoppers.remove(request.user)
        else :
            product.shoppers.add(request.user)
        return render(request, "interface/product_view.html", {
        "product": product,
        "added": product.shoppers.filter(pk=request.user.pk).exists(),
    })
    return render(request, "interface/product_view.html", {
        "product": product,
        "added": added,
    })

def about_us(request):
    return render(request, "interface/about_us.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "interface/login.html", {
                "response": "Oops! Invalid username/password."
            })
    else: 
        return render(request, "interface/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if (password != confirmation):
            return render(request, "interface/register.html", {
                "response": "Confirmation must match password",
            })
        try: 
            user = User.objects.create_user(username, email, password)
        except IntegrityError:
            return render(request, "interface/register.html", {
                "response": "Username/Email already taken",
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else: 
        return render(request, "interface/register.html")
    
@login_required
def shopping_cart(request):
    items = request.user.shopping_cart.all()
    return render(request, "interface/shopping_cart.html", {
        "items": items,
    })