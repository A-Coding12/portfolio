from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import send_mail
from email import message

# Create your views here.
def index(request):
    return render(request, "index.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            name,
            message,
            email,
            ['abdollahchegdali45@gmail.com'],
            fail_silently=False,
        )
        return render(request, "index.html", {'message_name' : name})

    else:
        return render(request, "index.html")
