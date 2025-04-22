import pytest

from product.models import Product
from product.serializers import ProductSerializer


@pytest.mark.django_db
def test_create_product(product_factory):
    product = product_factory()
    assert isinstance(product, Product)
    assert product.title
    assert product.price is not None


@pytest.mark.django_db
def test_product_serializer(product_factory):
    product = product_factory()
    serializer = ProductSerializer(product)
    data = serializer.data

    assert data["title"] == product.title
    assert data["description"] == product.description
    assert data["price"] == product.price
