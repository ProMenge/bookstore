import pytest 
from product.models import Category, Product
from product.factories import CategoryFactory, ProductFactory

@pytest.mark.django_db
def test_category_creation():
    category = CategoryFactory()
    assert Category.objects.count() == 1
    assert isinstance(category, Category)
    assert category.title is not None

@pytest.mark.django_db
def test_product_creation():
    product = ProductFactory()
    assert Product.objects.count() == 1
    assert isinstance(product, Product)
    assert product.title is not None
    assert product.price is not None
    assert product.categories is not None