import pytest

from product.serializers import CategorySerializer, ProductSerializer
from product.factories import CategoryFactory, ProductFactory

@pytest.mark.django_db
def test_category_serealizer():
    category = CategoryFactory()
    serizalizer = CategorySerializer(category)
    data = serizalizer.data
    assert data['slug'] == category.slug
    assert data['title'] == category.title
    
    
@pytest.mark.django_db
def test_product_serializer():
    product = ProductFactory()
    serializer = ProductSerializer(product)
    data = serializer.data
    assert data['title'] == product.title
    assert data['price'] == product.price
    assert isinstance(data['categories'], list)