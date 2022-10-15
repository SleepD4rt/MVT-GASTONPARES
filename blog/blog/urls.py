"""blog URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from family_member.views import create_family_member

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_family-member/<str:name>/<str:last_name>/<str:age>/<str:sex>/<str:height>/<str:profession>',
        create_family_member),
    path("family_member/", include("family_member.urls")),
]