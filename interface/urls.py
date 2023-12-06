from django.urls import path
from . import views
# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("blog/", views.blog, name="blog"),
    path("countdown/", views.countdown, name="countdown"),
    path("block_view/<int:block_id>", views.blog_view, name="blog_view")
]
