# API Layer (`src/api/`)

## Overview

The **API layer** is the gateway for external clients—such as frontend applications, mobile apps, or third-party services—to interact with the **Django Rwanda Portal system**.

Designed as a versioned **REST API**, this layer ensures backward compatibility and a clear upgrade path for future changes.

## The API layer is intentionally thin, handling only:

- Routing

- Versioning

- Schema definitions

- Delegating requests to the appropriate app logic

All **business logic** resides in the `apps` layer, maintaining a clean `separation of concerns`.

---

## Purpose

- Provide a **public interface** for all project features (`users`, `posts`, `comments`, etc.).

- Maintain API versioning (e.g., `/api/v1/...`) for smooth upgrades.

- Define and expose API schemas for clients via **OpenAPI/Swagger**.

- Route requests to the correct **app viewsets**.

---

#### Directory Structure

```python
src/api
├── __pycache__/
├── urls.py
└── v1/
    ├── __init__.py
    ├── routers.py
    ├── schema.py
    ├── tests.py
    └── views/
        ├── analytics.py
        ├── comments.py
        ├── events.py
        ├── media.py
        ├── messaging.py
        ├── posts.py
        ├── tags.py
        ├── users.py
        └── __init__.py
```

--- 

## Key Components

### 1. `urls.py`

The central entry point for API routes.

- Includes versioned routers (e.g., `v1.routers`).

- Example:

```python
from django.urls import path, include

urlpatterns = [
    path("v1/", include(("api.v1.routers", "v1"))),
]
```

### 2. `routers.py`

- Registers DRF `viewsets` for different apps.

- Keeps API endpoints organized and modular.

Example:

```python
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PostViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")
router.register(r"posts", PostViewSet, basename="posts")

urlpatterns = router.urls

```

3. `schema.py`

Generates OpenAPI/Swagger schema for API documentation.

Can be integrated with Swagger UI or ReDoc.

Example use: `/api/v1/schema/`.

4. `views/`

- Houses **generic API views** not tied to a specific app.

Examples:

- `HealthCheckView`: Returns server status.

- `APIRootView`: Lists available API endpoints.

Example Endpoints

Users

`POST /api/v1/users/` → Register a new user

`POST /api/v1/users/login/` → Login

`GET /api/v1/users/me/` → Fetch logged-in user profile

Posts

`GET /api/v1/posts/` → List all posts

`POST /api/v1/posts/` → Create a post

`GET /api/v1/posts/{id}/` → Retrieve a single post

Health Check

- `GET /api/v1/health/` → Returns `{"status": "ok"}`

---

## Contributor Guidelines

**Do not implement business logic in the app layer**. Keep it in the respective API view in src/api/v1/views.
The view is for each app separated with versioning with different 

Register new endpoints by adding `viewsets` to `routers.py`.

Update the OpenAPI schema (`schema.py`) when introducing new endpoints.

Ensure all new endpoints have tests in their respective apps.

#### Interactions with Other Layers

| Layer / Directory           | Interaction / Purpose                                                |
|-----------------------------|----------------------------------------------------------------------|
| `src/apps/`                 | Provides viewsets, serializers, and services exposed by the API.    |
| `src/core/`                 | Leverages core utilities to follow DRY principles.                  |
| `src/common/templates/`     | May provide API-related templates (e.g., email notifications).      |
| `src/config/urls.py`        | Includes `src/api/urls.py` as part of global URL routing.           |


---

## Next Steps for Development

- Implement **rate-limiting** and throttling.

- Add **API key authentication** for third-party integrations.

- Improve **API documentation** with Swagger UI or ReDoc.

- Introduce version 2 (`v2`) when breaking changes are required.

---

## Documentation Links

  - [API Layer](./api.md)

  - [Users App](./apps/users.md)

  - [Posts App](./apps/posts.md)

  - [Analytics App](./apps/analytics.md)

  - [Comments App](./apps/comments.md)

  - [Events App](./apps/event.md)

  - [Media App](./apps/media.md)

  - [Messaging App](./apps/messaging.md)

  - [Notifications App](./apps/notification.md)

  - [Tags App](./apps/tags.md)

  - [Common Layer](./common.md)

  - [Config Layer](./config.md)

  - [Core Layer](./core.md)

  - [Development Guide](../DEVELOPMENT_GUIDE.md)

---

## License
Django Rwanda is released under the [MIT License](../LICENSE).

### Copyright (c) 2025 I. Fils 