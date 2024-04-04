from django.urls import path
from . import views

urlpatterns = [
    path('404/', views.err_404, name='err-404'),
    path('faq/', views.faq, name='faq'),
    path('terms/', views.terms, name='terms'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact),
]
