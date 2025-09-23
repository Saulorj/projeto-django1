from django.conf.urls import handler400, handler403, handler404, handler500
from django.urls import path

from . import views

# urls.py do projeto
handler404 = views.error_404_view
handler500 = views.error_500_view
handler403 = views.error_403_view
handler400 = views.error_400_view

app_name = 'main'

urlpatterns = [
    path('', views.main_view, name='home'),
    path('search/', views.search, name='search'),
    path('recipes/<int:id>/', views.recipe, name='recipe'),
    path('category/<int:id>/', views.category, name='category'),


    # fixas
    path('sobre/', views.sobre_view, name='sobre'),
    path('contato/', views.contato_view, name='contato'),
]