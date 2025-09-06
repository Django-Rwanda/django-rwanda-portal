# Comments App

## Overview

The **Comments app** manages all functionality related to **user comments** across the platform.  
It allows users to:
- Comment on **posts**, **events**, or other content.
- Reply to other comments (nested/threaded comments).
- Interact with comments (edit, delete, report, moderate).
- Expose comment data via **API endpoints** for frontend/mobile clients.

By isolating comments into their own app, we ensure:
- **Reusability** (comments can be attached to multiple apps like posts, media, or events).
- **Extensibility** (future features such as likes, mentions, or moderation can be added easily).
- **Separation of concerns** (business logic stays out of `posts`, `events`, etc.).

---

## Purpose
- Store and manage **user-generated comments**.
- Enable **threaded/nested discussions**.
- Provide **API endpoints** for CRUD operations.
- Integrate with **notifications** (e.g., notify when someone replies to your comment).
- Support **moderation** tools (flagging, soft deletion).

---

## Directory Structure

```bash
src/apps/comments
├── admin.py # Admin registration for comments
├── apps.py # App configuration
├── filters.py # Filters for searching and querying comments
├── forms.py # Django forms for admin or web UI
├── migrations/ # Database migrations
├── models/ # Defines Comment model
│ └── init.py
├── selectors.py # Read/query logic for comments
├── serializers.py # DRF serializers for API requests/responses
├── services.py # Business logic (create, update, delete, reply)
├── signals.py # Signals (e.g., notify on new comment)
├── static/ # App-specific static files (if any)
├── tasks.py # Celery tasks (async notifications, moderation jobs)
├── templates/ # Templates for email or UI rendering
├── tests/ # Unit/integration tests
│ ├── models.py
│ ├── serializers.py
│ ├── tasks.py
│ └── views.py
├── urls.py # Routes for views endpoints
└── views.py # template views for comment CRUD
```

---

## Key Features

### 1. Comment Model
- **Fields**:
  - `author` → ForeignKey to `users.User`
  - `content` → Text of the comment
  - `parent` → Self-referential ForeignKey (for replies)
  - `object_id` + `content_type` → Generic relation (so comments can attach to posts, events, media, etc.)
  - `is_deleted` → Soft-delete flag
  - `created_at`, `updated_at`
- **Supports nesting** via `parent` relationship.

### 2. Services (`services.py`)
Encapsulates core operations:
- Create a new comment.
- Edit an existing comment.
- Soft delete a comment.
- Reply to a comment.

### 3. Selectors (`selectors.py`)
Provides reusable read queries:
- List comments for a post or event.
- Get all replies for a given comment.
- Fetch comments by user.

### 4. Serializers (`serializers.py`)
Converts comment data to/from JSON for API.
- Example: Nest replies within parent comment.

### 5. Views & URLs
- Exposed via API (`/api/v1/comments/`).
- Typical endpoints:
  - `POST /comments/` → Create a comment.
  - `GET /comments/?post_id=123` → List comments for a post.
  - `PUT /comments/{id}/` → Edit a comment.
  - `DELETE /comments/{id}/` → Soft delete a comment.

If you need to add new api endpoint, you will need to add it's view and route to specific version in `src/api/version`

### 6. Signals
- Notify post/event author when a new comment is added.
- Trigger moderation tasks if flagged.

### 7. Tasks
- Asynchronous email/notification sending.
- Background moderation jobs (spam detection).

---

## Example Usage

### Creating a Comment (Service Layer)

```python
from apps.comments import services

comment = services.create_comment(
    author=user,
    content="This is my comment!",
    target_object=post  # could be a Post, Event, etc.
)
```

### Fetching Comments (Selector Layer)

```python
from apps.comments import selectors

comments = selectors.get_comments_for_object(post)
```

---

## Contributor Guidelines

- Follow the project’s `coding standards` (see `CONTRIBUTING.md`).

- Always use services.py for business logic, not directly in views.

- Keep queries in selectors, not in views.

- Use soft delete (is_deleted=True) instead of removing rows permanently.

- Ensure comments are linked generically so they can attach to multiple content types.

- Ensure new features have tests in `tests/`.

---

## Interactions with Other Apps

- Users → Each comment belongs to a user.

- Posts / Events / Media → Comments can attach to these objects.

- Notifications → Sends alerts when a comment is created or replied to.

- Analytics → Tracks engagement (number of comments per post).

- Next Steps for Development

- Add comment likes/reactions.

- Support mentions (`@username`) and notify mentioned users.

- Integrate with moderation tools (spam filters, AI toxicity detection).

- Add pagination & sorting for large comment threads.

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