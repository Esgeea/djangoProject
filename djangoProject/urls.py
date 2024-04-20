"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

from userextend.forms import AuthenticationNewForm

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('prefix/', include('intro.urls'))  -> daca vrem un prefix
    path('', include('intro.urls')),
    path('', include('home.urls')),
    path('', include('student.urls')),
    path('', include('trainer.urls')),
    path('', include('module.urls')),
    path("login/", views.LoginView.as_view(form_class=AuthenticationNewForm), name="login"),
    path('', include('django.contrib.auth.urls')),



    path('', include('userextend.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Aceasta linie de cod ( static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)) face parte din config. fisierelor
# din media si utilizat pentru a asigura afisarea corecta a fisierelor media

# Functia static primeste 2 args:

# primul argument (settings.MEDIA_URL) -> reprezinta url de baza pentru fisierele din folderul media
# al doilea argument(settings.MEDIA_ROOT) -> reprezinta folderul fizic in care sunt stocate fisierele

# In concluzie, serverul va prelua fisierele media prin intermediul url specificat
