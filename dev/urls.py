from django.conf.urls import include
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import path

urlpatterns = [
    path('account/', include('account.urls', namespace='account')),
    path('admin/', admin.site.urls),
    path('static/<path:path>', serve, name='static'),
]
