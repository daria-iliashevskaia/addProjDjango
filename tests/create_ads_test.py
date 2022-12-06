import pytest


@pytest.mark.django_db
def test_create_ads(client, ads, JWT_token):

    data = {
            "id": 8,
            "author": ads.author.username,
            "category": ads.category.name,
            "name": "testtesttest",
            "price": 100,
            "description": "testtesttesttesttesttest",
            "is_published": False,
            "image": None
            }

    data_to_send = {
            "author": ads.author.username,
            "category": ads.category.name,
            "name": "testtesttest",
            "price": 100,
            "description": "testtesttesttesttesttest",
            "is_published": False
            }

    response = client.post('/ad/create/',
                           data_to_send,
                           content_type="application/json",
                           HTTP_AUTHORIZATION="Bearer " + JWT_token)

    assert response.status_code == 201
    assert response.data == data