import pytest

from ads.models import User, Category

from tests.factories import UserFactory, CategoryFactory, AdsFactory


@pytest.mark.django_db
def test_create_ads(client, ads):
    author = User.objects.create(
                        password="1234",
                        first_name="test",
                        last_name="test",
                        username="username",
                        age=24
                        )
    category = Category.objects.create(
                        name="test",
                        slug="test",
                        )

    data = {
            "id": ads.id,
            "author": author.username,
            "category": category.name,
            "name": "testtesttest",
            "price": 100,
            "description": "testtesttesttesttesttest",
            "is_published": False,
            "image": None
            }

    data_to_send = {
            "author": author.username,
            "category": category.name,
            "name": "testtesttest",
            "price": 100,
            "description": "testtesttesttesttesttest",
            "is_published": False
            }

    # author = UserFactory.create()
    # category = CategoryFactory.create()

    response = client.post('/ad/create/',
                           data_to_send,
                           content_type="application/json")

    assert response.status_code == 201
    assert response.data == data