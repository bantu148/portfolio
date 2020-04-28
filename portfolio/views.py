from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import form

# Create your views here.
def index(request):
    return render(request, 'index.html')

def submit(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    subject = request.POST.get("subject")
    message = request.POST.get("message")
    new_item = form(name=name, email=email, subject=subject, message=message)
    new_item.save()
    return HttpResponseRedirect("/")