from django.db.models import F
from utils.filterset import SearchFilterSet

from apps.menu.models import Food


class FoodFilter(SearchFilterSet):

    class Meta:
        model = Food
        fields = (
        )

    def filter_queryset(self, queryset):
        qs = super().filter_queryset(queryset)
        # qs = qs.order_by('-create_dt')
        # qs = qs.filter(article_id=self.request.parser_context['kwargs']['article_id'])
        # qs = qs.annotate(author_fio=F('author__fio'))
        return qs