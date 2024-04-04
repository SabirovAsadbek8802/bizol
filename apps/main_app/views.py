from django.shortcuts import render

def err_404(request):
    return render(request, '404.html')


def faq(request):
    return render(request, 'faq.html')

def about(request):
    return render(request, 'about.html')

def terms(request):
    return render(request, 'terms.html')


def contact(request):
    return render(request, 'contact.html')
