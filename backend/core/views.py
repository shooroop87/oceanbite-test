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

class HealthView(View):
    def get(self, request):
        return JsonResponse({"status":"ok"})
