from django.test import TestCase
from django.urls import resolve, reverse


# Create your tests here.
class MainURLsTest(TestCase):
    def test_the_pytest_is_ok(self):
        assert 1 == 1, 'Check if pytest is working'

    def test_main_url_is_correct(self):
        main_url = reverse('main:home')
        assert main_url == '/', 'Check if main URL is correct'

    def test_recipe_and_category_is_correct(self):
        recipe_url = reverse('main:recipe', kwargs={'id': 1})
        category_url = reverse('main:category', kwargs={'id': 1})
        assert recipe_url == '/recipes/1/', 'Check if recipe URL is correct'
        assert category_url == '/category/1/', 'Check if category URL is correct'

class MainViewsTest(TestCase):
    def test_main_view_function_is_correct(self):
        main_url = reverse('main:home')
        found = resolve(main_url)
        assert found.func.__name__ == 'main_view', 'Check if main view function is correct'

    def test_recipe_view_function_is_correct(self):
        recipe_url = reverse('main:recipe', kwargs={'id': 1})
        found = resolve(recipe_url)
        assert found.func.__name__ == 'recipe', 'Check if recipe view function is correct'

    def test_category_view_function_is_correct(self):
        category_url = reverse('main:category', kwargs={'id': 1})
        found = resolve(category_url)
        assert found.func.__name__ == 'category', 'Check if category view function is correct'