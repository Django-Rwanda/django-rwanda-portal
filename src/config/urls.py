"""
URL configuration for src project.

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
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
    

def home(request):
    return render()


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(("api.urls", "api"))),

    # Apps
    # path("analytics/", include(("apps.analytics.urls", "analytics"))),
    # path("comments/", include(("apps.comments.urls", "comments"))),
    # path("events/", include(("apps.events.urls", "events"))),
    # path("media/", include(("apps.media.urls", "media"))),
    # path("messaging/", include(("apps.messaging.urls", "messaging"))),
    # path("notifications/", include(("apps.notifications.urls", "notifications"))),
    # path("posts/", include(("apps.posts.urls", "posts"))),
    # path("tags/", include(("apps.tags.urls", "tags"))),
    # path("users/", include(("apps.users.urls", "users"))),
]


if settings.DEBUG:
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))