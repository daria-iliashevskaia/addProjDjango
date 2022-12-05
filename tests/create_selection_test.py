import pytest

from ads.serializers import SelectionsSerializer


@pytest.mark.django_db
def test_create_selection(client, selections):
    data = {
            "id": selections.pk,
            "items": [],
            "owner": None,
            "name": "test chooses"
            }
    data_to_send = {
       "name": selections.name
    }

    response = client.post('/selections/create/',
                           data_to_send,
                           content_type="application/json")

    assert response.status_code == 201
    assert response.data == data