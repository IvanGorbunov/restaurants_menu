from django.db.models import Count
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APITestCase

from apps.menu.tests.factories import ToppingFactory, FoodCategoryFactory, FoodFactory

from apps.menu.models import Topping, FoodCategory, Food


class ViewTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 10 toppings
        number_of_toppings = 10
        toppings = []
        for topping_id in range(number_of_toppings):
            toppings.append(ToppingFactory(
                    name=f'Topping: {topping_id}',
                )
            )

        # Create 5 categories
        number_of_categories = 5
        categories = []
        for category_id in range(number_of_categories):
            categories.append(FoodCategoryFactory(
                    name=f'Category: {category_id}',
                    is_publish=category_id <= 3,
                )
            )

        FoodFactory(
            name='Food: 1',
            category=categories[0],
            # toppings=[i.id for i in toppings[:4]],
            is_publish=True,
            is_special=False,
            is_vegan=False,
        ).toppings.set(toppings[:4])

        FoodFactory(
            name='Food: 2',
            category=categories[0],
            # toppings=toppings[2:7],
            is_publish=True,
            is_special=True,
            is_vegan=False,
        ).toppings.set(toppings[2:7])

        FoodFactory(
            name='Food: 3',
            category=categories[1],
            # toppings=toppings[5:7],
            is_publish=True,
            is_special=True,
            is_vegan=True,
        ).toppings.set(toppings[5:7])

        FoodFactory(
            name='Food: 4',
            category=categories[1],
            # toppings=toppings[5:7],
            is_publish=False,
            is_special=True,
            is_vegan=True,
        ).toppings.set(toppings[5:7])

        FoodFactory(
            name='Food: 5',
            category=categories[2],
            # toppings=toppings[5:7],
            is_publish=False,
            is_special=True,
            is_vegan=True,
        ).toppings.set(toppings[5:7])

        FoodFactory(
            name='Food: 6',
            category=categories[4],
            # toppings=toppings,
            is_publish=False,
            is_special=False,
            is_vegan=False,
        ).toppings.set(toppings)

    def test_list_01_url_exists_at_desired_location(self):
        response = self.client.get('/api/v1/menu/')
        self.assertEqual(response.status_code, 200, response.data)

    def test_list_02_url_accessible_by_name(self):
        response = self.client.get(reverse_lazy('menu:list'))
        self.assertEqual(response.status_code, 200, response.data)

    def test_list_03_all_items(self):
        response = self.client.get(reverse_lazy('menu:list'))
        self.assertEqual(response.status_code, 200, response.data)

        if response.status_code != 200:
            return

        foods_categories = FoodCategory.objects.filter(is_publish=True)
        foods_categories = foods_categories.annotate(foods_count=Count('foods'))
        foods_categories = foods_categories.exclude(foods_count=0)
        foods_categories = foods_categories.all()
        a = 1

        self.assertNotEqual(response.data, [], response.data)
        self.assertEqual(len(response.data), foods_categories.count(), response.data)

    def test_list_04_is_vegan(self):
        response = self.client.get(reverse_lazy('menu:list') + '?is_vegan=True')
        self.assertEqual(response.status_code, 200, response.data)

        if response.status_code != 200:
            return

        foods_categories = FoodCategory.objects.filter(is_publish=True, foods__is_vegan=True)
        foods_categories = foods_categories.annotate(foods_count=Count('foods'))
        foods_categories = foods_categories.exclude(foods_count=0)
        foods_categories = foods_categories.all()
        a = 1

        self.assertNotEqual(response.data, [], response.data)
        self.assertEqual(len(response.data), foods_categories.count(), response.data)
