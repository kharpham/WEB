from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "interface/commerce.html")

def blog(request):
    return render(request, "interface/blog.html")