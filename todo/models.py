from django.db import models


# Create your models here.
class Item(models.Model):
    # blank=false prevents creation of todo items without a name
    # null=false prevents items created without a name programmatically
    name = models.CharField(max_length=50, null=False, blank=False)
    # to make sure to-do items are marked as not done by default.
    done = models.BooleanField(null=False, blank=False, default=False)

    # override default model string method from Django to change how
    # items are displayed. It takes in self which is the class itself
    # as its own argument and will return the item class's name attribute
    # which is the name that we put into the form. Doing this will make sure
    # that in the admin site we see our item names instead of item object.
    def __str__(self):
        return self.name
