from django.urls import path

from . import loader, views

urlpatterns = [
    path(selector.path, views.view_fabric(selector).as_view())
    for selector in loader.selectors
]
