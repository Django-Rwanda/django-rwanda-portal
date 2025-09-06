from django.urls import path, include

app_name = "api"


urlpatterns = [
    # API Version 1
    path("v1/", include(("api.v1.routers", "v1"), namespace="v1")),
]
