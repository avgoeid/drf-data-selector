from rest_framework import response, views

from . import models


def method(selector):
    def inner(request, *args, **kwargs):
        data = models.fetchall(selector)

        return response.Response(data)

    return inner


def view_fabric(selector):
    view = type(
        selector.__name__ + views.APIView.__name__,
        (views.APIView,),
        {
            selector.method: method(selector),
        },
    )

    return view
