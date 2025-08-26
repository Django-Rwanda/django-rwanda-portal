from django.urls import path, include
from core.utils.constants import greet
from core.db.mixins import child

app_name = "api"

urlpatterns = [
    path("analytics/", include(("apps.analytics.urls", "analytics"))),
    # path("comments/", include(("apps.comments.api", "comments"))),
    # path("events/", include(("apps.events.api", "events"))),
    # path("media/", include(("apps.media.api", "media"))),
    # path("messaging/", include(("apps.messaging.api", "messaging"))),
    # path("notifications/", include(("apps.notifications.api", "notifications"))),
    # path("posts/", include(("apps.posts.api", "posts"))),
    # path("tags/", include(("apps.tags.api", "tags"))),
    # path("users/", include(("apps.users.api", "users"))),
]

print(greet())

print(child().__class__.__name__ + "s")