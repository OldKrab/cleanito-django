"""djangoProject URL Configuration

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
from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.HomeView.as_view(), name='index'),
    path('user-ads', views.UserAdsView.as_view(), name='user-ads'),
    path('ad/<int:pk>', views.AdInfoView.as_view(), name='ad'),
    path('ad/<int:pk>/update', views.AdUpdateView.as_view(), name='ad-update'),
    path('ad/<int:pk>/delete', views.AdDeleteView.as_view(), name='ad-delete'),
    path('ad/create', views.AdCreateView.as_view(), name='ad-create'),
]
