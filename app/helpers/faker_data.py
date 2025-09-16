
from itertools import count
from random import randint

from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)

fake = Faker('pt_BR')
seq = count(0)


_imgs = ["https://foodish-api.com/images/burger/burger1.jpg",
"https://foodish-api.com/images/idly/idly69.jpg",
"https://foodish-api.com/images/butter-chicken/butter-chicken10.jpg",
"https://foodish-api.com/images/pasta/pasta11.jpg",
"https://foodish-api.com/images/burger/burger32.jpg",
"https://foodish-api.com/images/pizza/pizza82.jpg",
"https://foodish-api.com/images/dosa/dosa74.jpg"]

def image_iterator(images):
    index = 0
    while True:
        yield images[index]
        index = (index + 1) % len(images)  # volta para 0 quando chega ao final

next_image = image_iterator(_imgs)

def make_recipe():
    return {
        'id': next(seq),
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porção',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url': next(next_image),
        }
    }

def make_recipes(qtd=10):
    recipes = [make_recipe() for _ in range(qtd)]
    return recipes