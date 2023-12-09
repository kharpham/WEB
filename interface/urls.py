from django.urls import path
from . import views
# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("blog/", views.blog, name="blog"),
    path("countdown/", views.countdown, name="countdown"),
    path("blog_view/<int:blog_id>", views.blog_view, name="blog_view"),
    path("product_view/<int:product_id>", views.product_view, name="product_view"),
    path("about_us/", views.about_us, name="about_us"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
]

