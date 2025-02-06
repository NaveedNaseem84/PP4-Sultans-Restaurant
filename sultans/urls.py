"""
URL configuration for sultans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from welcome import views as index_views
from aboutus import views as aboutus_views
from book import views as book_views
from menu import views as menu_views

urlpatterns = [
    path('', index_views.index, name='index'),
    path('aboutus/', aboutus_views.index, name='aboutus'),
    path('book/', book_views.index, name='book'),
    path('menu/', menu_views.index, name='menu'),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
]
