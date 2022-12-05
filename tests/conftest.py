from pytest_factoryboy import register
from tests.factories import AdsFactory, UserFactory, CategoryFactory, SelectionsFactory

pytest_plugins = "tests.fixtures"

register(AdsFactory, _name='ads')
register(UserFactory, _name='user')
register(CategoryFactory, _name='category')
register(SelectionsFactory, _name='selections')

