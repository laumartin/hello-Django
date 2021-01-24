"""django_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # the url triggers say hello function and return http response to browser
    # To do that we use the built-in path function which takes three arguments:
    # The url that the user is going to type in. In our case hello
    # The view function to be returned, say_hello
    # The name parameter
    path('', views.get_todo_list, name='get_todo_list'),
    path('add', views.add_item, name='add'),
    # <> these is the mechanism by which the item ID makes its way from
    # links or forms in our templates through the URL and into the view
    # which expects it as a parameter.
    path('edit/<item_id>', views.edit_item, name='edit'),
    path('toggle/<item_id>', views.toggle_item, name='toggle'),
    path('delete/<item_id>', views.delete_item, name='delete')
]
