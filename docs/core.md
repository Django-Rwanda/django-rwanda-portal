# Core App (`src/core/`)

## Overview

The `Core` app serves as the foundation of the Django Rwanda Portal.
It provides **infrastructure-level building blocks** that other apps depend on, ensuring `consistency`, `maintainability`, and `reusability` across the entire project.

Unlike feature apps (e.g., `users`, `posts`), the **core/ app** focuses only on **shared utilities and system-wide abstractions** such as database tools, middleware, and security helpers.

---

## Key goals of `core/`:

✅ Enforce DRY principles (Don’t Repeat Yourself).

✅ Provide consistent patterns across all apps.

✅ Make global changes (e.g., `database mixins`, `middleware`) easy to manage.


```bash
📂 Directory Structure
src/core
├── db
│   ├── fields.py
│   ├── managers.py
│   ├── mixins.py
│   ├── models.py
│   ├── routers.py
│   └── __init__.py
├── middleware
│   ├── request_logging.py
│   ├── timing.py
│   └── __init__.py
├── security
│   ├── jwt.py
│   └── __init__.py
├── utils
│   ├── constants.py
│   ├── exceptions.py
│   └── __init__.py
└── tests
    ├── test_db.py
    ├── test_middleware.py
    ├── test_security.py
    ├── test_utils.py
    └── __init__.py

```

## 🔑 Key Components
### 1. `core/db/`

#### Reusable database utilities.

- `fields.py` → Custom fields (`EncryptedTextField`, `LowercaseEmailField`).

- `managers.py` → Query managers (`.active()`, `.archived()`).

- `mixins.py` → Abstract models (`TimeStampedMixin`, `UUIDMixin`).

- `routers.py` → Database routers (useful for **multi-database setups**).

### Usage Example:

```python
from core.db.mixins import TimeStampedMixin
    

class Post(TimeStampedMixin):
    title = models.CharField(max_length=200)
```

### 2. `core/middleware/`

#### Custom middlewares to enhance request/response lifecycle.

`request_logging.py` → Logs incoming requests & responses.

`timing.py` → Measures request execution time.

Usage Example (settings):

```python
MIDDLEWARE = [
    "core.middleware.request_logging.RequestLoggingMiddleware",
    "core.middleware.timing.TimingMiddleware",
    ...
]
```

### 3. `core/security/`

Security-related utilities.

`jwt.py` → JWT authentication helpers.

### 4. `core/utils/`

#### Generic project-wide utilities.

`constants.py` → Global constants (roles, statuses).

`exceptions.py` → Base exception classes for consistent error handling.

#### Example:

```python
from core.utils.exceptions import AppBaseException

class InvalidAction(AppBaseException):
    code = "invalid_action"
    message = "This action is not allowed."
```

### 5. `core/tests/`

#### Centralized testing for core features.

- Uses **`pytest`** + **`pytest-django`**.

- Mirrors the structure of `core/` for clarity.

- Each module has its own dedicated test file.

---

## ✅ Contribution Guidelines

- Add logic here only if reusable across multiple apps.

    - ✔ `TimeStampedMixin` → belongs in `core.db.mixins`.

    - ✘ User-specific validation → stays in `users/`.

- Avoid putting **business/domain** logic in `core/`.

- Keep modules **small and focused**.

- Always update documentation when introducing new utilities.

---

## 🌍 Interaction with Other Layers

- **Apps** (`src/apps/`) → Import database mixins, managers, fields.

- **API** (`src/api/`) → Uses core.security.jwt for authentication.

- **Config** (`src/config/settings/`) → Registers core middlewares, exceptions, and JWT logic.

---

## 🚀 Future Improvements

- Add **rate-limiting middleware**.

- Add **audit logging** in `core/db/`.

- Create a **global caching utility** for apps.

---

## Documentation

- [API Layer](./api.md)

-  **Apps – includes**:

    - [Users](./apps/users.md)

    - [Posts](./apps/posts.md)

    - [Analytics](./apps/analytics.md)

    - [Comments](./apps/comments.md)

    - [Events](./apps/event.md)

    - [Media](./apps/media.md)

    - [Messaging](./apps/messaging.md)

    - [Notifications](./apps/notification.md)

    - [Tags](./apps/tags.md)

- [Common Layer](./common.md)

- [Config Layer](./config.md)

- [Core Layer](./core.md)

- [Development Guide](../DEVELOPMENT_GUIDE.md)

---

## License

This project is licensed under the [MIT License](../LICENSE)

### Copyright (c) 2025 I. Fils