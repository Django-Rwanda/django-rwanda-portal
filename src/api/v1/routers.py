from django.urls import path, include
from django.http import JsonResponse, HttpResponse



app_name = "v1"

def testing_view(request):
    return HttpResponse("API is working!")

urlpatterns = [
    path("", testing_view, name="test-api"),
    path("add", lambda request: HttpResponse("hello world"), name="add-api"),
]

