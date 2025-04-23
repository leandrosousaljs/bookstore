import pytest
from product.factories import ProductFactory
from order.factories import OrderFactory


@pytest.fixture
def product_factory():
    return ProductFactory


@pytest.fixture
def order_factory():
    return OrderFactory
