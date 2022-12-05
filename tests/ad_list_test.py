import pytest

from ads.serializers import AdsSerializer
from tests.factories import AdsFactory


@pytest.mark.django_db
def test_ad_list(client):
    ads = AdsFactory.create_batch(5)

    data = {
            "count": 5,
            "next": None,
            "previous": None,
            "results": AdsSerializer(ads, many=True).data
            }
    response = client.get("/ad/")

    assert response.status_code == 200
    assert response.data == data
