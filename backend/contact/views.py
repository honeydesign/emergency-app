from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')

def addContact(request):
    if request.method == 'POST':
        new_contact = Contact(
            full_name = request.POST['fullname'],
            relationship = request.POST['relationship'],
            email = request.POST['email'],
            phone_number = request.POST['phone'],
            address = request.POST['address']
        )
        new_contact.save()
        return redirect('/main-contact')

    return render(request, 'new.html')

def mainContact(request):
    contacts = Contact.objects.all()
    return render(request, 'contact.html', {'contacts':contacts})

def contactProfile(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, 'contactprofile.html', {'contact': contact})

def editContact(request, pk):
    contact = Contact.objects.get(id=pk)
    
    if request.method == 'POST':
        contact.full_name = request.POST['fullname']
        contact.relationship = request.POST['relationship']
        contact.email = request.POST['email']
        contact.phone_number = request.POST['phone']
        contact.address = request.POST['address']
        contact.save()

        return redirect('/profile/'+str(contact.id))
    return render(request, 'edit.html', {'contact': contact})

def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('/')
    return render(request, 'delete.html', {'contact': contact})

