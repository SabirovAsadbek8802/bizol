from django.shortcuts import render
from .models import Category

def err_404(request):
    return render(request, '404.html')

def faq(request):
    return render(request, 'faq.html')

def about(request):
    return render(request, 'about.html')

def terms(request):
    return render(request, 'terms.html')

def home(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})

def contact(request):
    return render(request, 'contact.html')
