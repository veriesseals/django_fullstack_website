"""
URL configuration for devsearch project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include

# The urlpatterns list routes URLs to views.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    # The above line includes the URL patterns from the projects app.
    # This means that any URL that starts with '' (the root URL) will be handled
    # by the URL patterns defined in projects/urls.py.
]


