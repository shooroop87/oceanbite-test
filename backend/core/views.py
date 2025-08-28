from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def sustainability(request):
    return render(request, "core/sustainability.html")

def contacts(request):
    return render(request, "core/contacts.html")

def faq(request):
    return render(request, "core/faq.html")

def shipping_delivery(request):
    return render(request, "core/shipping_delivery.html")

def legal(request):
    return render(request, "core/legal.html")

def privacy(request):
    return render(request, "core/privacy.html")

def accessibility(request):
    return render(request, "core/accessibility.html")

def sitemap(request):
    return render(request, "core/sitemap.html")

class HealthView(View):
    def get(self, request):
        return JsonResponse({"status":"ok"})