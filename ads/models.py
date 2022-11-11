from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name='Имя')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Location(models.Model):

    name = models.CharField(max_length=100, verbose_name='Имя')
    lat = models.CharField(max_length=80, verbose_name='Ширина')
    lng = models.CharField(max_length=80, verbose_name='Долгота')

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class User(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, blank=True, verbose_name='Фамилия')
    username = models.CharField(max_length=100, verbose_name='Логин')
    password = models.CharField(max_length=100, verbose_name='Пароль')
    role = models.CharField(max_length=100, verbose_name='Роль')
    age = models.SmallIntegerField(verbose_name='Возраст')
    location = models.ManyToManyField(Location, null=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Ads(models.Model):

    name = models.CharField(max_length=100, verbose_name='Имя')
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(max_length=255, blank=True, verbose_name='Описание')
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True)
    image = models.ImageField(upload_to='images/', default='No images')
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
