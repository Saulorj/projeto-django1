from django.contrib import admin

from .models import Category, Recipe

# Register your models here.

#Category - Maneira simples
class CategoryAdmin(admin.ModelAdmin):
    ...
admin.site.register(Category, CategoryAdmin)


#Recipe - Maneira com anotation
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'is_published', 'category', 'created_at')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category', 'author')
    search_fields = ('title', 'author__username', 'category__name')
    list_per_page = 20
