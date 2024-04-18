from django.shortcuts import render, redirect
from .models import Category
from apps.store_app.models import Product
from .forms import OrderForm
from twilio.rest import Client
from django.http import HttpResponse


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
    products = Product.objects.all()
    return render(request, 'index.html', {
        'categories': categories,
        'products': products
        })

def contact(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order_instance = form.save() 
            # Send SMS notification
            send_sms_notification(order_instance)
            return HttpResponse("SMS notification sent successfully!")
    else:
        form = OrderForm()    
    return render(request, 'contact.html', {"form" : form})



def send_sms_notification(order_instance):
    account_sid = 'AC25dd490625f73182b5c3871a15f51172'
    auth_token = 'f68673fd92aad0d658b0a82960e899f2'
    client = Client(account_sid, auth_token)

    # Format the message with order data
    message_body = f"New order received:\n"
    message_body += f"Order ID: {order_instance.id}\n"
    message_body += f"Username: {order_instance.username}\n"
    message_body += f"Phone Number: {order_instance.phone_number}\n"
    message_body += f"Product: {order_instance.product}\n"
    message_body += f"Quantity: {order_instance.quantity}\n"
    message_body += f"Date: {order_instance.date}\n"
    message_body += f"Status: {order_instance.status}\n"
    # Add more fields as needed
    # Replace 'from_number' with your Twilio phone number and 'to_number' with your own phone number
    message = client.messages.create(
        body=f"\n\n\n\n\n {message_body}",
        from_='+14086375836',
        to='+998885108802'
    )