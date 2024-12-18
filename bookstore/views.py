from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

import git


@csrf_exempt
def update(request):
    if request.method == "POST":
        '''
        pass the path of the directory where your project will be
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "test.pythonanywhere.com"
        '''
        repo = git.Repo('/home/drsantos20/bookstore')
        origin = repo.remotes.origin

        origin.pull()
        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")


def hello_world(request):
    template = loader.get_template('hello_world.html')
    return HttpResponse(template.render())


def order_detail(request, pk):
    # Implement your logic for order_detail view
    return HttpResponse(f"Order detail for order ID: {pk}")


def product_detail(request, pk):
    # Implement your logic for product_detail view
    return HttpResponse(f"Product detail for product ID: {pk}")


def category_list(request):
    # Implement your logic for category_list view
    return HttpResponse("Category list")


def category_detail(request, pk):
    # Implement your logic for category_detail view
    return HttpResponse(f"Category detail for category ID: {pk}")