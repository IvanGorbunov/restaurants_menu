from django.db import models


class Topping(models.Model):
    """ Модель ингридиентов """
    name = models.CharField('Наименование ингридиента', null=False, max_length=350)

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'
        ordering = [
            'name',
        ]

    def __str__(self) -> str:
        return f'Ингридиент: {self.name} - {self.id}'


class FoodCategory(models.Model):
    """ Модель категорий блюд """
    name = models.CharField('Наименование блюда', null=False, max_length=350)
    is_publish = models.BooleanField('Опубликована', default=False)

    class Meta:
        verbose_name = 'Категория блюда'
        verbose_name_plural = 'Категории блюд'
        ordering = [
            'name',
        ]

    def __str__(self) -> str:
        return f'Категория: {self.name} - {self.id}'


class Food(models.Model):
    """ Модель блюда """
    name = models.CharField('Наименование ингридиента', null=False, max_length=350)
    category = models.ForeignKey(FoodCategory, verbose_name='Категория блюда', related_name='foods', on_delete=models.PROTECT)
    description = models.TextField('Описание', blank=True, null=True)
    price = models.IntegerField('Цена', default=0)

    is_special = models.BooleanField('Специальное', default=False)
    is_vegan = models.BooleanField('Вегитарианское', default=False)
    is_publish = models.BooleanField('Опубликовано', default=False)

    toppings = models.ManyToManyField(Topping, verbose_name='Ингридиенты', related_name='foods', blank=True)

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = [
            'name',
        ]

    def __str__(self) -> str:
        return f'Блюдо: {self.name} - {self.id}'

