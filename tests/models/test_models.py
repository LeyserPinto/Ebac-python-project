import pytest

from order.factories import OrderFactory


# @pytest.fixture
# def category_creation():
#     category = Category.objects.create(title = 'Pytest1', slug = 'Pytest1', description = 'teste')
#     assert category.title == 'Pytest1'
#     return category

# @pytest.mark.django_pytest
# def product_factory_creation():
#     factoryCategory = category_creation()    
#     instance_product_factory = ProductsFactory(category = factoryCategory)

#     assert instance_product_factory.price > 0

@pytest.fixture
def order_factory():
    return OrderFactory()

@pytest.mark.django_pytest
def django_test_order_factory(order_factory):
    product = order_factory.product()
    assert product.price > 1