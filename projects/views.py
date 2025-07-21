from django.shortcuts import render
# Importing HttpResponse to create a simple view function
# ------------------------------------
from django.http import HttpResponse

# Create your views here.

# These functions will become our URL patterns.
# Each path() function maps a URL to a view function.
# The first argument is the URL pattern, the second is the view function,
# and the third is an optional name for the URL pattern.
# The admin site is included by default, allowing access to the Django admin interface.
# ------------------------------------

def projects(request):
    # This is a function for the projects view.
    # You would typically return a rendered template or a response here.
    return render(request, 'projects/projects.html')

def project(request, pk):
    return render(request, 'projects/single-project.html')