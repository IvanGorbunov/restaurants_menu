import string

import factory.fuzzy
from factory.django import DjangoModelFactory

from apps.menu.models import Topping, FoodCategory, Food


class ToppingFactory(DjangoModelFactory):
    """
    Фабрика ингридиента
    """
    class Meta:
        model = Topping

    name = factory.fuzzy.FuzzyText(length=120)


class FoodCategoryFactory(DjangoModelFactory):
    """
    Фабрика Категорий блюд
    """
    class Meta:
        model = FoodCategory

    name = factory.fuzzy.FuzzyText(length=120)


class FoodFactory(DjangoModelFactory):
    """
    Фабрика блюда
    """
    class Meta:
        model = Food

    name = factory.fuzzy.FuzzyText(length=120)
    category = factory.SubFactory(FoodCategoryFactory)
    description = factory.fuzzy.FuzzyText(length=500)
    price = factory.fuzzy.FuzzyInteger(0, 10000, step=50)
