from django.contrib import admin
# from .models import Client
from .models import Client, Order

admin.site.register(Client)


class OrderAdmin(admin.ModelAdmin):
	model = Order
	list_display = ['client', 'created_at', 'finished']
	list_editable = ['finished']
	fields = ['client', 'created_at', 'updated_at', 'description', 'finished']
	readonly_fields = ['created_at', 'updated_at']


admin.site.register(Order, OrderAdmin)
