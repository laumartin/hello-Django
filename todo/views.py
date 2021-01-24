from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm
# Create your views here.


def get_todo_list(request):
    # This is going to allow us to use the item model in our views
    # we get a query set of all items in the db by creating a variable
    items = Item.objects.all()
    # this variable is a dictionary with all items in it, it needs
    # a key of items and that value is going to be our items variable created
    context = {
        'items': items
    }
    # render function takes an HTTP request and a template name as arguments
    # And it returns an HTTP response which renders that template.
    # we add context as 3rd argument to render the function and this
    # will ensure that we have access to it in our todo list.html template
    return render(request, "todo/todo_list.html", context)

# when somebody hits this add_item URL they end up in this add_item view.
# If it's a get request then we'll just return the add_item HTML template
# by rendering it to them. But if it's a post request we'll get the information
# from the form that comes from this template and use it to create a new item.
# And then we'll redirect them back to the get todo list view.


def add_item(request):
    # add if statement in add_item view to check what type of request this is.
    # if the request to this URL is a post request that mean it came
    # from someone clicking submit button on our form. And we want to actually
    # create a to-do item and redirect back to the home page to show the user
    # their updated to-do lists.
    if request.method == 'POST':
        # django creating the form
        form = ItemForm(request.POST)
        # call is_valid method on the form Django will automatically compare
        # data submitted in the post request to the data required on the model.
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm()
    context = {
            'form': form
        }
    return render(request, "todo/add_item.html", context)


# along with taking in the request. This view will also take item ID parameter
# And that's the item ID we just attached to the Edit link.
def edit_item(request, item_id):
    # get a copy of the item from db using built in django get_object_or_404
    # which we'll use to get an instance of the item model with an ID equal to
    # item ID that was passed into the view via the URL.
    # This method will return the item if it exists. Or 404 not found if not.
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        # django creating the form giving specific instance we want to update
        form = ItemForm(request.POST, instance=item)
        # call is_valid method on the form Django will automatically compare
        # data submitted in the post request to the data required on the model.
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    # create an instance of itemForm and return it to the template in context
    # we can pass an instance argument to the form telling it should be
    # prefilled with info for the item we got from db, defined in previous line
    form = ItemForm(instance=item)
    context = {
            'form': form
        }

    return render(request, 'todo/edit_item.html', context)


# this is called same as the views path in urls.py
# when a user clciks toggle our view will get the item
# and if it's done status is true it will flip it to false and viceversa
def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save
    return redirect('get_todo_list')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')
