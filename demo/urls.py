"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from myapp.views import *

from Cars.views import *
from category.views import *

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from product.views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', home),
    path('about/', about),
    path('services/', services),
    path('contact/', contact),
    path("login/",login),

    path('about1/', about1, name="about1"),
    path('contact1/', contact1, name="contact1"),

    path('delete-car/<int:id>/', delete_car, name="delete_car"),
    path('update-car/<int:id>/', update_car, name="update_car"),
    path('Cars/',Cars, name='Cars'),
    path('demo/', demo),
    path('get/', get),

    path('register/', register),
    path('dd/', dd),
    path('success/', success),
    path('category-show/', category_show),
    path('edit/<int:id>/', edit, name='edit'),
    path('delete/<int:id>/', delete, name='delete'),
    path('logout/', logout),

    path('mail/', mail),
    path('suggest-names/', suggest_names, name='suggest-names'),
    path('', home, name='home'),
    path('suggest-names/', suggest_names, name='suggest-names'),
    path('add/', add_person, name='add-person'),

]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()