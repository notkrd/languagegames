"""languagegames URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import index_view

urlpatterns = [
    url(r'^lindenmayergardens/', include('lindenmayergardens.urls'), name="lindenmayer-gardening"),
    url(r'^gamegames/', include('gamegames.urls'), name="gamegameing"),
    url(r'^fixedwords/', include('fixedwords.urls'), name="justwording"),
    url(r'^syntacticstrutting/', include('syntacticstrutting.urls'), name="syntacticstrutting"),
    url(r'^admin/', admin.site.urls, name="admin"),
    url(r'^$', index_view, name="home")
]

