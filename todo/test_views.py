from django.test import TestCase
from .models import Item
# Create your tests here.
# Every test will be defined as a method that begins with the word test.


class TestViews(TestCase):
    # it will take in self as its only parameter.Self here refers
    # to our TestViews class which because it inherits the test case class
    # wi'll have a bunch of pre-built methods we can use.
    def test_get_todo_list(self):
        # To test the HTTP responses of the views we can use a built-in
        # HTTP client that comes with the Django testing framework
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # To confirm the view uses the correct template,use
        # self.assertTemplateUsed and tell it the template we expect it
        # to use in the response.
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        # the URL will be edit followed by an item ID like 99 for example.
        # If we just pass it a static number the test will only pass if
        # that item ID exists in our db. To be more generic we need to
        # import the item model
        item = Item.objects.create(name='Test Todo Item')
        # Testing that we can get the Edit URL by adding on its ID
        # with the Python f string. They work almost identically to the
        # template literals in JavaScript lessons. Add an f before the
        # opening quotation mark and then anything we put in curly
        # brackets will be turned into part of the string.
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        response = self.client.post('/add', {'name': 'Test added Item'})
        # If the item is added successfully, the view should redirect
        # back to the home page.
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        # Since that item is the only one on the db and we just deleted
        # it.We can be certain the view works by asserting whether the
        # length of existing items is zero.
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        item = Item.objects.create(name='Test Todo Item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)

    def test_can_edit_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated Name')
