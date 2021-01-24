from django.contrib import admin
# from the current directories models file we want to import the item class.
from .models import Item

# Register your models here.
admin.site.register(Item)
