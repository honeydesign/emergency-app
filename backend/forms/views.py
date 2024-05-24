from django.shortcuts import render, redirect
from .models import Form

# Create your views here.

def index(request):
    return render(request, 'index.html')

def formDetails(request):
    if request.method == 'POST':
        new_form = Form(
            full_name = request.POST['fullname'],
            email = request.POST['email'],
            phone_number = request.POST['phone'],
            address = request.POST['address'],
            desc = request.POST['desc']
        )
        new_form.save()
        return redirect('/')

    return render(request, 'fire.html')