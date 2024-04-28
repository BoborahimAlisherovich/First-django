
from django.shortcuts import render
from django.contrib import messages
def home_view(request):
    return render(request, "index.html" )

def contact_view(request):
    return render(request, "contact.html" )

def news_view(request):
    return render(request, "news.html" )

def products_view(request):
    return render(request, "products.html" )

def services_view(request):
    return render(request, "services.html" )
