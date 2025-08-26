# Events App

## Overview

The **Events app** manages all functionality related to **event creation, participation, and discovery** within the Django Rwanda project.  
It provides tools for users to create, update, and manage events, while enabling others to RSVP, subscribe, or interact with them.

This app integrates tightly with **Users**, **Notifications**, and **Analytics** to provide a full event lifecycle.

---

## Purpose
- Allow users to **create and manage events**.
- Support **event participation** (RSVPs, ticketing, attendance tracking).
- Enable **discovery of events** by date, category, or location.
- Serve as a hub for **community engagement** (comments, media, reminders).
- Provide **data to analytics** for insights on participation and engagement.

---

## Directory Structure

```bash
src/apps/events
├── admin.py # Admin interface for managing events
├── apps.py # App configuration
├── filters.py # Event filtering (by date, location, category)
├── forms.py # Event creation/update forms
├── migrations/ # Database schema migrations
├── models/ # Event models (Event, RSVP, Category, Ticket, etc.)
├── selectors.py # Read/query logic (e.g., get_upcoming_events)
├── serializers.py # DRF serializers for API exposure
├── services.py # Business logic (create_event, RSVP, cancel_event)
├── signals.py # Event-driven hooks (e.g., notify attendees)
├── static/ # App-specific static files
├── tasks.py # Celery tasks (send reminders, async notifications)
├── templates/ # Templates for events (emails, HTML pages)
├── tests/ # Unit and integration tests
│ ├── models.py
│ ├── serializers.py
│ ├── tasks.py
│ └── views.py
├── urls.py # Routes for event endpoints
└── views.py # template views (event CRUD, RSVP, discovery)
```

---

## Key Features

### 1. Event Management
- Create, update, delete events.
- Support for recurring events (optional future extension).
- Categorization (e.g., tech meetup, training, social gathering).

### 2. Participation (RSVPs & Tickets)
- Users can RSVP or purchase tickets.
- Track attendance.
- Optional integration with payments (future).

### 3. Discovery
- List all upcoming events.
- Filter by **date, category, or location**.
- Personalized recommendations (via Analytics app).

### 4. Notifications
- Send reminders before event start.
- Notify users of changes/cancellations.
- Integrates with `notifications` app.

### 5. Integration Points
- **Users** → Event creators & participants.
- **Comments** → Users can comment on events.
- **Media** → Event images/videos.
- **Analytics** → Event attendance & popularity stats.

---

## Example Models

```python
from django.db import models
from django.conf import settings
from core.db.models import TimeStampedModel

class Event(TimeStampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name="events_created"
    )

    def __str__(self):
        return self.title

class RSVP(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="rsvps")
    status = models.CharField(
        choices=[("going", "Going"), ("interested", "Interested"), ("not_going", "Not Going")],
        max_length=20
    )
```

---

## Example Services

```python
from apps.events.models import Event, RSVP

def create_event(user, title, description, location, start_time, end_time):
    return Event.objects.create(
        created_by=user,
        title=title,
        description=description,
        location=location,
        start_time=start_time,
        end_time=end_time
    )

def rsvp_to_event(user, event, status="going"):
    return RSVP.objects.update_or_create(
        user=user,
        event=event,
        defaults={"status": status}
    )

```

---

## Example Selectors

```python
from django.utils import timezone
from apps.events.models import Event

def get_upcoming_events():
    return Event.objects.filter(start_time__gte=timezone.now()).order_by("start_time")

def get_events_by_user(user):
    return Event.objects.filter(created_by=user)

```

---

## Contributor Guidelines

- Follow the project’s `coding standards` (see `CONTRIBUTING.md`).

- Keep business logic in services.py, not in views.

- Add selectors for query logic instead of writing queries in views.

- Use signals to trigger notifications/reminders on event changes.

- Always write tests for new features (models, services, API).

- Maintain clear separation between event core logic and integration apps.

- Ensure new features have tests in `tests/`.

---

## Next Steps for Development

- Add recurring events support.

- Integrate payments for ticketed events.

- Build recommendation engine via analytics.

- Enable event live streaming/media integration.


