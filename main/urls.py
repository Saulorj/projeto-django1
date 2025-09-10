from django.urls import path
from django.conf.urls import handler404, handler500, handler403, handler400
from main import views as main_views

# urls.py do projeto
handler404 = main_views.error_404_view
handler500 = main_views.error_500_view
handler403 = main_views.error_403_view
handler400 = main_views.error_400_view

urlpatterns = [
    path('', main_views.main_view, name='main'),
    path('sobre/', main_views.main_view, name='sobre'),
    path('contato/', main_views.main_view, name='contato'),
]