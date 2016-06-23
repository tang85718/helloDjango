"""helloDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from home import views as home_view
from calc import views as calc_view

urlpatterns = [
    url(r'^$', home_view.home),
    url(r'^calc/', calc_view.add, name='add'),
    url(r'^calc_grace/(\d+)/(\d+)/$', calc_view.add_for_grace, name='add_for_grace'),
    url(r'^admin/', admin.site.urls),
]
