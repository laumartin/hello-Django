from django.test import TestCase
from .models import Item


# test that todo items will be created by default with
# the done status of false.
# Create class called TestModels which inherits TestCase.
class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='Test Todo Item')
        # to confirm that this name is returned when we render
        # this item as a string.
        self.assertEqual(str(item), 'Test Todo Item')

