from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name='Имя')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Ads(models.Model):

    name = models.CharField(max_length=100, verbose_name='Имя')
    author = models.CharField(max_length=100, verbose_name='Автор')
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(max_length=255, verbose_name='Описание')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


