# Tags App (`apps/tags/`)

The `Tags app` provides a centralized system for creating, managing, and associating tags with content across the Django Rwanda project. Tags are primarily used for categorization, search, filtering, and content organization.

## 📌 Purpose of `tags/`

Enable tagging functionality for posts, events, or other entities.

Provide a reusable model for tags that can be associated with multiple apps.

Support search, filtering, and content discovery based on tags.

Maintain consistent tagging logic through selectors, services, and serializers.

## 📂 Directory Structure

```bash
tags/
├── admin.py          # Tag admin registration for Django admin panel
├── apps.py           # Django app configuration
├── filters.py        # Query filters for tags
├── forms.py          # Forms for tag creation and editing
├── __init__.py
├── migrations/       # Database migration scripts
│   └── __init__.py
├── models/           # Base or modular models for tags
│   └── __init__.py
├── models.py         # Main Tag model
├── selectors.py      # Read/query logic for tags
├── serializers.py    # DRF serializers for API representation
├── services.py       # Business logic and operations on tags
├── signals.py        # Django signals related to tags
├── static/           # Static files (CSS, JS, images)
├── tasks.py          # Celery tasks related to tags
├── templates/
│   └── tags/         # Tag-specific templates
├── tests/            # Unit tests
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tasks.py
│   └── views.py
├── urls.py           # Tag-related URLs
└── views.py          # Views for tag operations
```

---

## 🔑 Key Components
1. Models

- Tag model defines:

    - name: Unique tag name.

    - slug: URL-friendly version.

    - Optional metadata (e.g., description, color, created_at).

    - Can be linked to other apps via Many-to-Many relationships.

2. Serializers

- Converts Tag objects to JSON for API responses.

- Supports validation for tag creation and updates.

3. Selectors

- Encapsulate querying logic for tags.

- Examples:

    - `get_all_tags()`

    - `get_tags_for_post(post_id)`

4. Services

- Business logic related to tags.

- Examples:

    - Assigning tags to posts.

    - Creating tags in bulk.

    - Ensuring tag uniqueness.

5. Filters

- Provides query filters for API endpoints.

- Supports searching, ordering, and filtering tags.

6. Signals

- Hooks for triggering events when tags are created or deleted.

- Example: updating associated content counts.

7. Views and URLs

- CRUD operations for tags (list, create, update, delete).

- Connected to API endpoints via src/api/version/urls.py.

8. Tasks

- Background tasks related to tag management.

- Example: updating tag statistics asynchronously.

---

## ✅ Contribution Guidelines

- Follow the project’s `coding standards` (see `CONTRIBUTING.md`).

- Adding New Features: Use services.py for business logic, not views.

- Query Logic: Keep read/query logic in selectors.py.

- API Changes: Update serializers.py and urls.py consistently.

- Testing: Always add tests in tests/ for models, serializers, and views.

- Signals: Only include app-wide behavior relevant to tags.

- Ensure tests exist for all new features (conversations, messages, services).


## 🚀 Examples of Usage

- Tagging a post:

```python
from apps.tags.models import Tag
from apps.posts.models import Post

tag = Tag.objects.create(name="Django")
post = Post.objects.first()
post.tags.add(tag)
```

## Filtering posts by tag in selectors:

```python
def get_posts_by_tag(tag_name):
    return Post.objects.filter(tags__name=tag_name)
```

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