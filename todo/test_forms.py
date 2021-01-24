from django.test import TestCase
from .forms import ItemForm
# Create your tests here.
# Every test will be defined as a method that begins with the word test.


# class TesItemForm will inherit Testcase and contain all tests for this form.
class TestItemForm(TestCase):
    # test to make sure name field is required in order to create an item.
    # name your tests so that when they fail you can identify the issue.
    def test_item_name_is_required(self):
        # A form that deliberately instantiate it without a name to simulate
        # a user who submitted the form without filling it out.
        form = ItemForm({'name': ''})
        # This form should not be valid,will use assert false to ensure that.
        self.assertFalse(form.is_valid())
        # When the form is invalid it should send back a dictionary of
        # fields on which there were errors and the Associated error messages
        # use assertIn to know if there's name key in dictionary of form errors
        # so the error occurred on the name
        self.assertIn('name', form.errors.keys())
        # use assertEqual to check whether the error message on the
        # name field is: this field is required. Use Zero index because
        # the form will return a list of errors on each field and this verifies
        # the first item in list is our string telling the field is required.
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    # ensure the done field is not required, it shouldn't be since it has
    # default value of false on the item model.
    def test_done_field_is_not_required(self):
        # Create form sending only a name,test that the form is valid as it
        # should be even without selecting a done status
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    # assume that another developer changes the item model adding a
    # field to it that contains some sort of information we don't want to
    # display on the form, we actually defined the fields to display
    # explicitly in the inner metaclass on the item form, form.py,otherwise the
    # form will display all fields on the model including those not for
    # the user to see. We should write a test to ensure that the only fields
    # that are displayed in the form are the name and done fields.
    def test_fields_are_explicit_in_form_metaclass(self):
        # we instantiate an empty form, use assert equal to check whether
        # the form.meta.fields attribute is = a list with name and done in it.
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
        