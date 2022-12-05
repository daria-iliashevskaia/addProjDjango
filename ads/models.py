from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils import timezone


def is_published_not_true(value):
    if value:
        raise ValidationError(
            'You can not publicate ads with "is_published" is True'
        )


def age_validator(value):
    now = timezone.now()

    if now.year - value.year < 9:
        raise ValidationError(
            "Your should be older then 9 years"
        )


class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name='Имя')
    slug = models.CharField(unique=True, max_length=10, validators=[MinLengthValidator(5)])

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
    birth_date = models.DateField(validators=[age_validator], null=True)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['username']

    def __str__(self):
        return self.username


class Ads(models.Model):

    name = models.CharField(max_length=100, verbose_name='Имя', validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена', validators=[MinValueValidator(0)])
    description = models.TextField(max_length=800, blank=True, verbose_name='Описание')
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True, validators=[is_published_not_true])
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
