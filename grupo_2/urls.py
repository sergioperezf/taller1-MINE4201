from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('menu.urls')),
    url(r'^taller_1', include('taller_1.urls')),
    url(r'^menu', RedirectView.as_view(url='/', permanent = True)),
]
