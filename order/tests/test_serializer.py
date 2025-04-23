import pytest 
from order.serializers import OrderSerializer
from order.factories import OrderFactory

@pytest.mark.django_db
def test_order_serializer():
    order = OrderFactory()
    serializer = OrderSerializer(order)
    data = serializer.data
    assert isinstance(data['product'], list)
    assert data['user'] == order.user.id
