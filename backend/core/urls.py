from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("sustainability/", views.sustainability, name="sustainability"),
    path("contacts/", views.contacts, name="contacts"),
    path("faq/", views.faq, name="faq"),
    path("shipping-delivery/", views.shipping_delivery, name="shipping_delivery"),
    path("legal/", views.legal, name="legal"),
    path("privacy/", views.privacy, name="privacy"),
    path("accessibility/", views.accessibility, name="accessibility"),
    path("sitemap/", views.sitemap, name="sitemap"),
]