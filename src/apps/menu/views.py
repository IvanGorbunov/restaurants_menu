from django.shortcuts import render

from apps.menu.models import Food
from utils.views import MultiSerializerViewSet

from apps.menu.filters import FoodFilter
from apps.menu.serializers import FoodListSerializer


class MenuViewSet(MultiSerializerViewSet):
    queryset = Food.objects.filter(is_publish=True)
    filtersets = {
        'list': FoodFilter,
    }
    serializers = {
        'list': FoodListSerializer,
    }

    def list(self, request, *args, **kwargs):
        """
        Список блюд
        """
        return super().list(request, *args, **kwargs)
