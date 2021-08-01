"""testsmagistratura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('isviv.urls')),
    path('istgv/', include('istgv.urls')),
    path('tosous/', include('tosous.urls')),
    path('gidravlika/', include('gidravlika.urls')),
    path('ecology/', include('ecology.urls')),
    path('oask/', include('oask.urls')),
    path('zakon/', include('zakon.urls')),
    path('vivmgsu/', include('vivmgsu.urls')),
    path('tezis/', include('tezis.urls')),
    path('geodezy/', include('geodezy.urls')),
    path('mathematics/', include('mathematics.urls')),
    path('metrology/', include('metrology.urls')),
    path('soilmechanics/', include('soilmechanics.urls')),
    path('mzhg/', include('mzhg.urls')),
    path('admin/', admin.site.urls),
]
