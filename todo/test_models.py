from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        # create an item and use assert false to confirm its 
        # done status is false.
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)
