from django import forms
from .models import Item


# Our form has a class that inherits a built-in Django class of formd.mdelform
class ItemForm(forms.ModelForm):
    # to tell the form which model is associated with, we provide meta class
    # gives our form some information about itself.Like which fields it should
    # render how it should display error messages and so on
    class Meta:
        model = Item
        # we want to display the name in done fields from the model.
        fields = ['name', 'done']

