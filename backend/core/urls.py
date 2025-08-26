from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("sustainability/", views.sustainability, name="sustainability"),
    path("contacts/", views.contacts, name="contacts"),
]
