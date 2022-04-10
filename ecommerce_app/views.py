from django.shortcuts import render

def home(request):
    
    return render(request, "ecommerce_app/home/home.html")
