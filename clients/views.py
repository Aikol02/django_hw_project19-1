from django.shortcuts import render
from .models import Client


def clients_list(request):
	context = {}
	client_list = Client.objects.all()
	context["client_list"] = client_list
	html_page = render(request, 'name.html', context)
	return html_page
