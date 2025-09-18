from django.shortcuts import get_object_or_404, render

from .models import Recipe

# Create your views here.


def main_view(request):
    _recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    context = {"recipes": _recipes}
    return render(request, 'main/home.html', context=context)

def category(request, id: int):
    _recipes = Recipe.objects.filter(category__id=id, is_published=True).order_by('-id')
    context = {"recipes": _recipes}
    return render(request, 'main/home.html', context=context)


def recipe(request, id: int):
    # _recipe =  Recipe.objects.get(id=id)
    _recipe = get_object_or_404(Recipe, pk=id, is_published=True)
    context={"recipe": _recipe, "is_detail_page": True}
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
