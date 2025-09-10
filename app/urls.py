"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf.urls import handler404, handler500, handler403, handler400
from main import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),

]

# urls.py do projeto
handler404 = main_views.error_404_view
handler500 = main_views.error_500_view
handler403 = main_views.error_403_view
handler400 = main_views.error_400_view
