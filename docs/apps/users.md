# Users App (`apps/users`)

## Overview
The **Users app** is the foundation of the Django Rwanda project. It manages **authentication, authorization, and user profiles**. This app is responsible for defining the **custom user model**, handling registration, login, and user-related services. It ensures that all user-related operations are centralized, secure, and extendable for future needs.

By isolating user management in its own app, we make the system **modular** and allow contributors to improve authentication without affecting other parts of the project.

---

## Purpose
- Provide a **custom user model** to support project-specific fields (e.g., phone, country, roles).
- Handle **authentication flows** (login, logout, password reset).
- Manage **user profiles** and role-based access (e.g., staff, admin, customer).
- Serve as the **integration point** for permissions and authentication tokens.
- Expose **API endpoints** for user-related actions (via the `api` layer).

---

## Directory Structure

```bash
src/apps/users
├── admin.py # User model admin registration for Django admin panel
├── apps.py # App configuration
├── filters.py # Filtering logic for user queries (e.g., search by country or role)
├── forms.py # Forms for user creation and updates
├── migrations/ # Database migrations for user model
├── models/ # Defines the custom User model and related models
├── selectors.py # Query-layer logic (read-only queries, e.g., get_user_by_email)
├── serializers.py # DRF serializers for converting user data to/from JSON
├── services.py # Business logic for user operations (create, update, deactivate)
├── signals.py # Event-driven logic (e.g., send email on user creation)
├── static/ # App-specific static files (if any)
├── tasks.py # Celery tasks (e.g., async email sending)
├── templates/ # Templates for user-related views/emails
├── tests/ # Unit and integration tests
│ ├── models.py
│ ├── serializers.py
│ ├── tasks.py
│ └── views.py
├── urls.py # URL routes for user endpoints
└── views.py # DRF views (e.g., registration, login, profile update)

```


---

## Key Features

### 1. Custom User Model
- Extends Django’s base user.
- Includes fields like:
  - `first_name`, `last_name`
  - `email` (used for login instead of username)
  - `phone`, `country`
  - Role flags: `is_admin`, `is_staff`, `is_customer`
- Provides **flexibility for future fields**.

### 2. Authentication
- Login and logout endpoints.
- Token-based authentication using **JWT**.
- Role-based access for staff vs. customers.

### 3. User Services
The `services.py` layer encapsulates business logic, such as:
- Creating a user with hashed passwords.
- Activating/deactivating accounts.
- Assigning user roles.

### 4. Query Selectors
The `selectors.py` layer provides **read-only queries**, e.g.:
- Get user by email.
- List all active users.
- Filter users by role or country.

### 5. Admin Panel
- Customized admin interface for managing users.
- Extended search and filtering by custom fields.

### 6. Signals
- Example: Send a welcome email after successful registration.
- Trigger background tasks when a user updates their profile.

---

## Example Usage

### Creating a New User (Service Layer)
```python
from apps.users import services

user = services.create_user(
    email="jane@example.com",
    password="securepassword",
    first_name="Jane",
    last_name="Doe",
    phone="+250780000000",
    country="Rwanda"
)

```

### Fetching a User (Selector Layer)


```python
from apps.users import selectors

user = selectors.get_user_by_email("jane@example.com")
```

## Contributor Guidelines

When contributing to the Users app:

  - Follow the project’s `coding standards` (see `CONTRIBUTING.md`).

  - Do not modify the user model fields directly without consensus (use migrations carefully).

  - Add new user-related services to services.py and keep views thin.

  - Write selectors for queries instead of placing raw queries in views.

  - Keep authentication logic stateless and rely on JWT.

  - Ensure all new features are covered with tests in the tests/ directory.

  - Follow best practices for security (e.g., never log passwords, use hashing).
  

## Interactions with Other Layers

- API Layer (src/api): Exposes user endpoints for frontend and external services.

- Core Layer (src/core/security/jwt.py): Provides JWT token utilities.

- Common Layer (src/common/emails): Handles templates for email confirmation, password reset.

- Other Apps:

   - posts: Users are authors of posts.

   - comments: Users write comments.

   - notifications: Users receive system notifications.


## Next Steps for Development

   - Add social login integration (Google, GitHub, etc.).

   - Enhance email verification with one-time codes or QR codes.

   - Improve admin UI with user analytics.

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