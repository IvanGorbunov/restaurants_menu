from apps.menu.models import Food, Topping, FoodCategory
from django.db.models import Count, Q
from rest_framework import serializers


class FoodToppings(serializers.ModelSerializer):

    class Meta:
        model = Topping
        fields = (
            'name',
        )

    def to_representation(self, instance):
        return instance.name


class FilteredFoodListSerializer(serializers.ListSerializer):

    def to_representation(self, instance):
        is_vegan = self.context['request'].query_params.get('is_vegan')
        if is_vegan:
            instance = instance.filter(is_vegan=is_vegan)
        is_special = self.context['request'].query_params.get('is_special')
        if is_special:
            instance = instance.filter(is_special=is_special)
        data = self.context['request'].data
        if data and isinstance(data, list):
            instance = instance.filter(toppings__name__in=data)
        return super().to_representation(instance)


class FoodListSerializer(serializers.ModelSerializer):
    toppings = FoodToppings(many=True, read_only=True)

    class Meta:
        list_serializer_class = FilteredFoodListSerializer
        model = Food
        fields = (
            'name',
            'description',
            'price',
            'is_vegan',
            'is_special',
            'toppings',
        )


class FilteredFoodCategoryListSerializer(serializers.ListSerializer):

    def to_representation(self, instance):
        instance = instance.annotate(foods_count=Count('foods'))
        instance = instance.exclude(foods_count=0)
        return super().to_representation(instance)


class FoodCategoryListSerializer(serializers.ModelSerializer):
    foods = FoodListSerializer(many=True, read_only=True)

    class Meta:
        list_serializer_class = FilteredFoodCategoryListSerializer
        model = FoodCategory
        fields = (
            'id',
            'name',
            'foods',
        )
