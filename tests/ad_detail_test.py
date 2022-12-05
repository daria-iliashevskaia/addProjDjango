import pytest


@pytest.mark.django_db
def test_ad_detail(client, ads):
    data =  {"id": ads.pk,
            "author": ads.author.username,
            "category": ads.category.name,
            "name": "testtesttest",
            "price": 100,
            "description": "testtesttesttesttesttest",
            "is_published": False,
            "image": None
            }

    response = client.get(f"/ad/{ads.pk}/")
    assert response.status_code == 200
    assert response.data == data