from django.contrib import admin
from django.urls import path
from clients.views import info, contacts, clients_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('admin/', admin.site.urls),
	path('info/', info),
	path('contacts/', contacts),
	path('clients/', clients_list),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
