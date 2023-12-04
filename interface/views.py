from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "interface/countdown.html")

def blog(request):
    return render(request, "interface/blog.html")