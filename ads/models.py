from django.contrib.auth.models import AbstractUser
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name='Имя')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Location(models.Model):

    name = models.CharField(max_length=100, verbose_name='Имя')
    lat = models.CharField(max_length=80, verbose_name='Ширина')
    lng = models.CharField(max_length=80, verbose_name='Долгота')

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.name


class User(AbstractUser):

    UNKNOWN = "unknown"
    MEMBER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"
    ROLE = [(UNKNOWN, "unknown"), (MEMBER, "member"), (MODERATOR, "moderator"), (ADMIN, "admin")]

    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, blank=True, verbose_name='Фамилия')
    username = models.CharField(max_length=100, verbose_name='Логин', unique=True)
    role = models.CharField(max_length=100, choices=ROLE, default=UNKNOWN, verbose_name='Роль')
    age = models.SmallIntegerField(verbose_name='Возраст', null=True)
    location = models.ManyToManyField(Location, null=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['username']

    def __str__(self):
        return self.first_name


class Ads(models.Model):

    name = models.CharField(max_length=100, verbose_name='Имя')
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(max_length=255, blank=True, verbose_name='Описание')
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name


class Selections(models.Model):

    name = models.CharField(max_length=100, verbose_name='Имя')
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ads, null=True)

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'

    def __str__(self):
        return self.name
