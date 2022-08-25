from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from .models import ContactLink, About
from .forms import ConTactForm


class ContactView(View):

    def get(self, request):
        contacts = ContactLink.objects.all()
        form = ConTactForm()
        return render(request, 'contact/contact.html', {"contacts": contacts, "form": form})


class CreateContact(CreateView):
    form_class = ConTactForm
    success_url = "/"


class AboutView(View):
    def get(self, request):
        about = About.objects.first()
        return render(request, 'contact/about.html', {"about": about})
