from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name = "home"),
    path("about", views.about, name = "about"),
    path('sending', views.email, name = "email"),
    path('send', views.send, name = "send")
]
