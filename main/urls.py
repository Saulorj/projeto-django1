from django.conf.urls import handler400, handler403, handler404, handler500
from django.urls import path

from . import views

# urls.py do projeto
handler404 = views.error_404_view
handler500 = views.error_500_view
handler403 = views.error_403_view
handler400 = views.error_400_view

urlpatterns = [
    path('', views.main_view, name='main'),
    path('recipes/<int:id>/', views.recipe, name='recipe'),

    # fixas
    path('sobre/', views.sobre_view, name='sobre'),
    path('contato/', views.contato_view, name='contato'),
]