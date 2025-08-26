# API Layer

## Overview
The **API layer** is the entry point for external clients (frontend applications, mobile apps, or third-party integrations) to interact with the **Django Rwanda** system. It is designed as a **versioned REST API**, ensuring backward compatibility and clear upgrade paths for future improvements.

This layer is **thin** by design: it only handles routing, schema definitions, and delegating requests to the appropriate app logic. All **business logic** is implemented inside the `apps` layer, ensuring separation of concerns.

---

## Purpose
- Provide a **public interface** for all project features (users, posts, comments, etc.).
- Ensure **API versioning** (e.g., `/api/v1/...`) for smooth evolution of endpoints.
- Define and document the **schema** for clients using OpenAPI/Swagger.
- Route incoming requests to the correct **app views**.

---

## Directory Structure

```bash
src/api
├── urls.py # Root API routing (entry point for all versions)
└── v1 # First API version
├── init.py
├── routers.py # DRF routers for apps
├── schema.py # OpenAPI/Swagger schema definitions
└── views.py # API-level views (e.g., health check, API root)
```


---

## Key Components

### 1. `urls.py`


- Central entry point for all API routes.
- Includes versioned routers (e.g., `v1.routers`).
- Example:

```python
  from django.urls import path, include

  urlpatterns = [
    path("v1/", include(("api.v1.routers", "v1"))),
  ]
```

### 2. `routers.py`

- Defines DRF routers for different apps.

- Ensures each app can register its endpoints without cluttering the API layer.

- Example:

```python
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from .views import PostViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")
router.register(r"posts", PostViewSet, basename="posts")

urlpatterns = router.urls
```

### 3. `schema.py`

- Generates the OpenAPI schema for API documentation.

- Allows integration with Swagger UI or ReDoc.

- Example use case: exposing /api/v1/schema/.

### 4. `views.py`

- Contains generic API views not tied to specific apps.

Examples:

   - HealthCheckView (returns server status).

   - APIRootView (lists available endpoints).

---

## Example Endpoints

- Users

  - POST /api/v1/users/ → Register a new user.

  - POST /api/v1/users/login/ → Login 

  - GET /api/v1/users/me/ → Fetch logged-in user profile.

- Posts

  - GET /api/v1/posts/ → List posts.

  - POST /api/v1/posts/ → Create a post.

  - GET /api/v1/posts/{id}/ → Retrieve a single post.

- Health Check

  - GET /api/v1/health/ → Returns {"status": "ok"}.

---

## Contributor Guidelines

When working with the API layer:

- **Do not implement business logic here.** Keep it in the respective app’s `services.py` or `views.py`.

Add new endpoints by registering viewsets in `routers.py`.

Always update the OpenAPI schema (`schema.py`) when new endpoints are introduced.

Ensure all new endpoints have `tests` in their respective app.

---

Interactions with Other Layers

Apps (`src/apps`): Provides viewsets and serializers that the API exposes.

Core (`src/core/`): Utilize the core functionalities to follow DRY principle.

Common (`src/common/templates`): May provide API-related templates (e.g., email confirmations).

Config (`src/config/urls.py`): Includes `src/api/urls.py` as part of global URL routing.

---

## Next Steps for Development

- Add rate limiting and throttling for API endpoints.

- Implement API key authentication for external integrations.

- Improve API documentation with Swagger UI or ReDoc.

- Add version 2 (`v2`) when breaking changes are introduced.