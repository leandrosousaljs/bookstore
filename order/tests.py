import pytest
from order.models import Order
from order.serializers import OrderSerializer


@pytest.mark.django_db
def test_create_order(order_factory, product_factory):
    product1 = product_factory()
    product2 = product_factory()
    order = order_factory(product=[product1, product2])

    assert isinstance(order, Order)
    assert order.user is not None
    assert order.product.count() == 2


@pytest.mark.django_db
def test_order_serializer(order_factory, product_factory):
    product1 = product_factory()
    product2 = product_factory()
    order = order_factory(product=[product1, product2])

    serializer = OrderSerializer(order)
    data = serializer.data

    assert len(data["product"]) == 2
    assert data["total"] == product1.price + product2.price
