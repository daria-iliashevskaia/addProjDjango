import pytest


@pytest.mark.django_db
def test_create_ads(client, JWT_token):
    data = {
            "id": 2,
            "author": "test",
            "category": "test",
            "name": "test",
            "price": 100,
            "description": "testtesttesttesttesttest",
            "is_published": False,
            "image": "test.png"
            }
    data_to_send = {
            "author": "test",
            "category": "test",
            "name": "test",
            "price": 100,
            "description": "testtesttesttesttesttest",
            "is_published": False,
            "image": "test.png"
            }
    response = client.post("/ad/create/",
                           data_to_send,
                           content_type="application/json",
                           HTTP_AUTHORIZATION = "Bearer"+ JWT_token)
    assert response.status_code == 201
    assert response.data == data