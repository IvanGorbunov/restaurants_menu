from apps.menu.models import Food, Topping
from rest_framework import serializers


class FoodToppings(serializers.ModelSerializer):

    class Meta:
        model = Topping
        fields = (
            'name',
        )

    def to_representation(self, instance):
        return instance.name


class FoodListSerializer(serializers.ModelSerializer):
    toppings = FoodToppings(many=True)

    class Meta:
        model = Food
        fields = (
            'name',
            'description',
            'price',
            'is_vegan',
            'is_special',
            'toppings',
        )
