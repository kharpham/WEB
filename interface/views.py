from django.shortcuts import render
from datetime import datetime, timedelta
from pytz import timezone
# Create your views here.
def index(request):
    now = datetime.now(timezone('Asia/Ho_Chi_Minh'))
    target_datetime = datetime(2023, 12, 5, 20, 0, 0, tzinfo=timezone('Asia/Ho_Chi_Minh'))
    if target_datetime < now:
        return render(request, "interface/countdown.html")
    else:
        return render(request,  "interface/commerce.html")
def blog(request):
    return render(request, "interface/blog.html")

