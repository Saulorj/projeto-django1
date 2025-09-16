from django.shortcuts import render

from app.helpers.faker_data import make_recipe, make_recipes

# Create your views here.
_recipes = make_recipes(7)

def main_view(request):
    context = {"recipes": _recipes}
    return render(request, 'main/home.html', context=context)

def recipe(request, id: int):
    context={"recipe": _recipes[id], "is_detail_page": True}
    return render(request, 'main/recipe-view.html', context=context)


# Views fixas
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
    return render(request, 'errors/400.html', status=400)
