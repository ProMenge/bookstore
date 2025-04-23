import pytest 
from order.models import Order
from order.factories import OrderFactory

@pytest.mark.django_db
def test_order_creation():
    order = OrderFactory()
    assert Order.objects.count() == 1
    assert isinstance(order, Order)
    assert order.user is not None
    assert order.product is not None