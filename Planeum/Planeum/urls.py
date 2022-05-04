"""Planeum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django import views
from django.conf import settings
from django.contrib import admin
from django.urls import URLPattern, path, include
from django.contrib.auth.decorators import login_required
#from todoapp.views import addTodoView, todoappView
from django.conf.urls.static import static
from requests import delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('register/', include('register.urls')),
    path('login/', include('login.urls')),
    path('chat/',include('chat.urls')),
    path('newsfeed/', include('newsfeed.urls')),
    path('accounts/', include('allauth.urls')),
    #path('', include('todoapp.urls')),
    #path('todoapp/', include('todoapp.urls')),
    #path('todoapp/list/', include('todoapp.urls')),
    path('userprofile/', include('userprofile.urls')),
    path('', include('base.urls')),
    path('base/', include('base.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
