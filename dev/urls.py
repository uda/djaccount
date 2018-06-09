from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.views import serve

urlpatterns = [
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^admin/', admin.site.urls),
    url(r'^static/(?P<path>.*)$', serve, name='static'),
]
