# Notifications App (`apps/notification`)

## Overview
The **Notifications app** handles all system and user-triggered notifications across the platform.  
It provides a **unified interface** for sending and managing notifications, regardless of delivery channel (in-app, email, SMS, push).  

This app ensures that users receive relevant updates (e.g., new comment on a post, event reminders, system alerts) in a **consistent, scalable, and asynchronous** manner.

---

## Purpose
- Manage **notification models** (in-app storage, metadata, read/unread state).
- Provide a **service layer** to send notifications across different channels.
- Allow **extensibility** for future delivery types (e.g., push, webhooks).
- Enable **asynchronous sending** via Celery tasks.
- Integrate with signals from other apps (`posts`, `comments`, `events`, etc.).

---

## Directory Structure

```bash
src/apps/notifications
├── admin.py # Notification model admin registration
├── apps.py # App config
├── filters.py # Filtering logic for querying notifications
├── forms.py # Forms for managing notifications in the admin
├── migrations/ # Database migrations
├── models/ # Defines Notification and related models
├── selectors.py # Read-only queries (e.g., get_unread_notifications)
├── serializers.py # DRF serializers for notifications
├── services.py # Business logic (send, mark read, broadcast)
├── signals.py # React to events (e.g., comment created → notify post author)
├── static/ # Static files (if any)
├── tasks.py # Celery async tasks for notification sending
├── templates/ # Templates for emails or in-app rendering
├── tests/ # Unit/integration tests
│ ├── models.py
│ ├── serializers.py
│ ├── tasks.py
│ └── views.py
├── urls.py # Endpoints for notifications url
└── views.py # Django views (list, mark as read, etc.)
```

---

## Key Features

### 1. Notification Model

- Represents a single notification event.
- Typical fields:
  - `recipient` (FK to `User`)
  - `actor` (FK to `User`, optional)
  - `verb` (short description, e.g., "commented on")
  - `target` (Generic FK to related object, e.g., `Post`)
  - `is_read` (boolean)
  - `created_at`

### 2. Delivery Channels

- **In-App:** Stored in DB, exposed via API.
- **Email:** Uses `common/emails` templates.
- **SMS / Push:** Extensible via service integrations.

### 3. Service Layer (`services.py`)

Encapsulates logic like:
- Sending a new notification.
- Marking notifications as read/unread.
- Bulk sending (e.g., event reminder to many users).

### 4. Selectors

Read-only queries for consumers:
- `get_unread_notifications(user)`
- `get_recent_notifications(user, limit=10)`

### 5. Signals

Listen to events in other apps and trigger notifications:
- Comment created → notify post author.
- New event → notify all subscribers.
- System alert → notify admins.

### 6. Async Tasks

- Offload sending to Celery for performance.
- Example: send email notification after comment is created.

---

## Example Usage

### Sending a Notification

```python
from apps.notifications import services

services.send_notification(
    recipient=user,
    actor=author,
    verb="commented on",
    target=post,
    channel=["in_app", "email"]
)
```

### Fetching Notifications

```bash
from src.apps.notifications import selectors

unread = selectors.get_unread_notifications(user=request.user)
```

---

## API Endpoints

- GET /api/v1/notifications/ → List notifications.

- POST /api/v1/notifications/mark-read/ → Mark selected as read.

- GET /api/v1/notifications/unread-count/ → Get unread count.

If you need to add new api endpoint, you will need to add it's view and route to specific version in `src/api/version`

---

## Contributor Guidelines

- Keep views thin: use services.py and selectors.py for business/query logic.

- Add new delivery channels in services.py, not in views.

- Always write Celery tasks for sending heavy notifications (avoid blocking requests).

- Use signals to hook into events from other apps.

- Ensure new features have tests in `tests/`.

---

## Interactions with Other Apps

- Users: Recipients of notifications.

- Posts/Comments: Generate notifications when new content is created.

- Events: Event reminders and updates.

- Messaging: Direct messages can trigger notifications.

- Common/Emails: Provides email templates.

---

## Next Steps for Development

- Add real-time notifications via WebSockets (e.g., Django Channels).

- Add mobile push notification support.

- Implement notification preferences (user can choose channel types).

- Create digest emails for daily/weekly summaries.

---

## Documentation

- [API Layer](../api.md)

-  **Apps – includes**:

    - [Users](./users.md)

    - [Posts](./posts.md)

    - [Analytics](./analytics.md)

    - [Comments](./comments.md)

    - [Events](./event.md)

    - [Media](./media.md)

    - [Messaging](./messaging.md)

    - [Notifications](./notification.md)

    - [Tags](./tags.md)

- [Common Layer](../common.md)

- [Config Layer](../config.md)

- [Core Layer](../core.md)

- [Development Guide](../../DEVELOPMENT_GUIDE.md)

---

## License

This project is licensed under the [MIT License](../../LICENSE)

### Copyright (c) 2025 I. Fils