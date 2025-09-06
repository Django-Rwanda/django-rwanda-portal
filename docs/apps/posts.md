# Posts App (`apps/posts`)

## Overview

The **posts app** is responsible for managing user-generated content within the Rwanda Community platform.
It enables members of the community to create, share, update, and interact with posts. Posts serve as the core content type around which discussions, comments, likes, and tags are built.

---

## Features

- Create, edit, and delete posts.

- Support for text, images, and links (via the Media app).

- Integration with tags for categorization.

- Connection with `comments` and `likes/reactions`.

- Visibility rules (public, private, or restricted to groups).

- API endpoints for CRUD operations and listing posts.

---

## Models

Core models typically include:

## - Post

      - title: Short title for the post.

      - content: Main body of the post.

      - author: Linked to the User model.

      - created_at / updated_at: Timestamps.

      - status: Draft, Published, Archived.

      - visibility: Public, Private, or Group-specific.

# - PostMedia (optional, linked to Media app)
    Used for attaching images, documents, or videos to a post.

---

## API Endpoints

Example API endpoints (subject to project’s router structure):

- `GET /api/posts/` → List all posts

- `POST /api/posts/` → Create a post

- `GET /api/posts/{id}/` → Retrieve a specific post

- `PUT /api/posts/{id}/` → Update a post

- `DELETE /api/posts/{id}/` → Delete a post

Future extensions:

- `GET /api/posts/{id}/comments/`

- `POST /api/posts/{id}/like/`

If you need to add new api endpoint, you will need to add it's view and route to specific version in `src/api/version`

---

## Relationships with Other Apps

- Users → Each post belongs to a registered user.

- Comments → Posts can have threaded comments.

- Tags → Posts can be tagged for categorization.

- Notifications → Triggered when someone comments or reacts.

- Analytics → Track engagement, post popularity, and activity.

---


## Permissions & Access Control

- `Authenticated users` can create posts.

- `Owners` can edit or delete their own posts.

- `Admins/Moderators` can manage posts across the platform.

- Posts may have `visibility rules` (e.g., only visible to certain groups).

---

## Example Serializer (DRF)

```python
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "content", "author", "created_at", "updated_at", "status", "visibility"]
        read_only_fields = ["id", "author", "created_at", "updated_at"]

```

---

## Contribution Guidelines

When contributing to this app:

1. Follow the project’s `coding standards` (see `CONTRIBUTING.md`).

2. Add or update unit tests for all changes.

3. Document new API endpoints in the API docs.

4. Ensure migrations are included when modifying models.

5. Coordinate with maintainers if adding cross-app dependencies.

6. Ensure new features have tests in `tests/`.

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