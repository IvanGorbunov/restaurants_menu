from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.menu.models import Food, FoodCategory, Topping


@admin.register(Food)
class FoodAdmin(ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'price',
        'is_special',
        'is_vegan',
        'is_publish',
    )
    list_filter = (
        'is_special',
        'is_vegan',
        'is_publish',
    )
    search_fields = (
        'name',
        'category',
    )
    list_per_page = 25
    list_display_links = (
        'id',
        'name',
    )


@admin.register(FoodCategory)
class FoodCategoryAdmin(ModelAdmin):
    list_display = (
        'id',
        'name',
        'is_publish',
    )
    list_filter = (
        'is_publish',
    )
    search_fields = (
        'name',
    )
    list_per_page = 25
    list_display_links = (
        'id',
        'name',
    )


@admin.register(Topping)
class ToppingAdmin(ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    search_fields = (
        'name',
    )
    list_per_page = 25
    list_display_links = (
        'id',
        'name',
    )
