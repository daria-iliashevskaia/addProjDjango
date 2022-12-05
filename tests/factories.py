import factory
from factory.django import DjangoModelFactory
from ads.models import Ads, User, Category, Selections


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    password = "1234"
    first_name = "test"
    last_name = "test"
    username = factory.Faker("name")
    age = 24


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = "test"
    slug = factory.Faker("color")


class AdsFactory(DjangoModelFactory):
    class Meta:
        model = Ads

    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
    name = "testtesttest"
    price = 100
    description = "testtesttesttesttesttest"
    is_published = False


class SelectionsFactory(DjangoModelFactory):
    class Meta:
        model = Selections

    name = "test chooses"
