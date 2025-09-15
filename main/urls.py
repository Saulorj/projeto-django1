from django.urls import path
from django.conf.urls import handler404, handler500, handler403, handler400
from .views import *

# urls.py do projeto
handler404 = error_404_view
handler500 = error_500_view
handler403 = error_403_view
handler400 = error_400_view

urlpatterns = [
    path('', main_view, name='main'),
    path('sobre/', sobre_view, name='sobre'),
    path('contato/', contato_view, name='contato'),
]