from django.shortcuts import render

def home(request):
    
    return render(request, "ecommerce_app/home/home.html")

def viewItem(request):
    
    return render(request, "ecommerce_app/product_view/viewItem.html")