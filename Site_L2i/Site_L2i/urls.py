"""Site_L2i URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# from cgitb import html
# from msilib.schema import LockPermissions
from django.contrib import admin
from django.urls import path, include,re_path
from face import views
from django.urls import path
from django.conf import settings
# from django.conf.urls import url 
from django.views.static import serve
from django.conf.urls.static import static
from django.urls import re_path as url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('face', include('face.urls')),
    path('', views.index),
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    path('accounts/', include('accounts.urls')),
   # path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    