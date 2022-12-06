import pytest


@pytest.mark.django_db
def test_create_selection(client, selections, JWT_token):
    data = {
            "id": 2,
            "items": [],
            "owner": None,
            "name": "test chooses"
            }

    data_to_send = {
       "name": selections.name
    }

    response = client.post('/selections/create/',
                           data_to_send,
                           content_type="application/json",
                           HTTP_AUTHORIZATION="Bearer " + JWT_token)

    assert response.status_code == 201
    assert response.data == data