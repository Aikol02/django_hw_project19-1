from django.shortcuts import render
from .models import Client


def contacts(request):
	return render(request, "contacts.html")


def info(request):
	return render(request, "info.html")


def clients_list(request):
	context = {}
	client_list = Client.objects.all()
	context["client_list"] = client_list
	return render(request, 'clients.html', context)
