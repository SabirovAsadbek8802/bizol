from django.shortcuts import render

def err_404(request):
    return render(request, '404.html')


def faq(request):
    return render(request, 'faq.html')

# def index(request):
#     return render(request, 'index.html')

def terms(request):
    return render(request, 'terms.html')