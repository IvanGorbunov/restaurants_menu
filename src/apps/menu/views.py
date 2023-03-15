from apps.menu.models import FoodCategory
from utils.views import MultiSerializerViewSet

from apps.menu.serializers import FoodCategoryListSerializer


class MenuViewSet(MultiSerializerViewSet):
    queryset = FoodCategory.objects.filter(is_publish=True)
    serializers = {
        'list': FoodCategoryListSerializer,
    }

    def list(self, request, *args, **kwargs):
        """
        Список блюд по категориям
        """
        return super().list(request, *args, **kwargs)
