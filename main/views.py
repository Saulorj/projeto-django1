from django.shortcuts import render

# Create your views here.

def main_view(request):
    context = {}
    context['title'] = 'Página Principal'
    return render(request, 'main/home.html', context=context)

def sobre_view(request):
    context = {}
    context['title'] = 'Página SOBRE'
    return render(request, 'main/sobre.html', context=context)

def contato_view(request):
    context = {}
    context['title'] = 'Página CONTATO'
    return render(request, 'main/contato.html', context=context)

def error_404_view(request, exception):
    return render(request, 'errors/404.html', status=404)

def error_500_view(request):
    return render(request, 'errors/500.html', status=500)

def error_403_view(request, exception):
    return render(request, 'errors/403.html', status=403)

def error_400_view(request, exception):
    return render(request, 'errors/400.html', status=400)
