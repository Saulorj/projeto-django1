from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from app.helpers.pagination import make_pagination, make_pagination_range
from app.helpers.parser_help import int_get

from .models import Recipe

# Create your views here.


def main_view(request):
    _recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    page, pages = make_pagination(request, _recipes, per_page=3, qty_page=3)
    context = {"recipes": page, "pages": pages, 'search_term': ''}

    # messages.debug(request, "🐞 Esta é um debug")
    # messages.error(request, "❌ Este é um erro!!!")
    # messages.info(request, "👉 Esta é uma informação")
    # messages.success(request, "✅ Esta é um sucesso")
    # messages.warning(request, "⚠️ Esta é um aviso")

    return render(request, 'main/home.html', context=context)

def category(request, id: int):
    _recipes = Recipe.objects.filter(category__id=id, is_published=True).order_by('-id')
    page, pages = make_pagination(request, _recipes, per_page=3, qty_page=3)
    context = {"recipes": page, "pages": pages, 'search_term': ''}
    return render(request, 'main/home.html', context=context)

def recipe(request, id: int):
    # _recipe =  Recipe.objects.get(id=id)
    _recipe = get_object_or_404(Recipe, pk=id, is_published=True)
    context={"recipe": _recipe, "is_detail_page": True}
    return render(request, 'main/recipe-view.html', context=context)

def search(request):



    search_term = request.GET.get('q', '').strip()
    if not search_term:
        raise Http404()
    _recipes = Recipe.objects.filter(title__icontains=search_term, is_published=True).order_by('-id')
    page, pages = make_pagination(request, _recipes, per_page=3, qty_page=3)
    context = {"recipes": page, "pages": pages, "search_term": search_term, "add_qry": f'&q={search_term}'}
    return render(request, 'main/search.html', context=context)


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
    return render(request, 'errors/400.html', status=400)
    return render(request, 'errors/400.html', status=400)
