from django.urls import include, path

urlpatterns = [path("api/", include("drf_data_selector.urls"))]
