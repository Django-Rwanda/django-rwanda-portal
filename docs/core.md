# Core App (`src/core/`)

## Overview
The **Core app** provides the **low-level building blocks** and **infrastructure code** that other apps depend on.  
It is not a place for domain logic (like `users` or `posts`), but rather a collection of **shared, reusable components**: database utilities, middleware, security tools, and generic helpers.

By centralizing these concerns, the `core/` app ensures:
- **Consistency** across all apps.
- **DRY principles** (Don’t Repeat Yourself).
- **Maintainability** when making changes that affect the entire project.

---

## 📂 Directory Structure

```bash
src/core
├── db/ # Database abstractions
│ ├── fields.py # Custom model fields (e.g., encrypted, JSON, etc.)
│ ├── managers.py # Custom model managers (e.g., ActiveManager)
│ ├── mixins.py # Abstract model mixins (e.g., TimeStampedMixin)
│ ├── models.py # Shared abstract base models
│ ├── routers.py # DB routers for multi-database setups
│ └── init.py
│
├── middleware/ # Custom middlewares
│ ├── request_logging.py # Logs requests for debugging/monitoring
│ ├── timing.py # Tracks request execution time
│ └── init.py
│
├── security/ # Security-related utilities
│ ├── jwt.py # JWT handling (token generation, validation)
│ └── init.py
│
├── utils/ # Generic helper utilities
│ ├── constants.py # Project-wide constants
│ ├── exceptions.py # Custom exception classes
│ └── init.py
└── init.py

```

---

## 🔑 Key Components

### 1. `core/db/`

- Provides **reusable database components**:
  - `fields.py`: Custom fields like `EncryptedTextField`, `LowercaseEmailField`.
  - `managers.py`: Custom query managers (e.g., `.active()` for filtering active objects).
  - `mixins.py`: Common mixins like `TimeStampedMixin` or `UUIDMixin`.
  - `routers.py`: Database router logic (useful for **multi-database deployments**).

- **Usage Example**:
```python
  from core.db.mixins import TimeStampedMixin

  class Post(TimeStampedMixin):
      title = models.CharField(max_length=200)
```

### 2. `core/middleware/`

- Houses custom middlewares for request/response lifecycle.

    - request_logging.py: Logs incoming requests and responses.

    - timing.py: Measures execution time per request.

Usage Example (settings):

```python
MIDDLEWARE = [
    "core.middleware.request_logging.RequestLoggingMiddleware",
    "core.middleware.timing.TimingMiddleware",
    ...
]
```

### 3. `core/security/`

- Handles security-related utilities.

### 4. `core/utils/`

- Generic utilities available across the project:

    - constants.py: Global constants (roles, statuses, etc.).

    - exceptions.py: Base exception classes for consistent error handling.

Example:

```python
from core.utils.exceptions import AppBaseException

class InvalidAction(AppBaseException):
    code = "invalid_action"
    message = "This action is not allowed."

```

## ✅ Contribution Guidelines

- Add logic here only if it is project-wide reusable.
Example: a custom TimeStampedMixin → goes to core.db.mixins.
Example: email validation for users → stays in users, not in core.

- Do not put business/domain logic inside core/.

- Keep modules small and focused (avoid dumping unrelated helpers).

- Update this documentation when adding new core features.

## 🌍 Interactions with Other Layers

- Apps (src/apps/):
Use core.db mixins, managers, and custom fields.
Middleware is automatically applied to all app requests.

- API (`src/api/`):
  Relies on core.security.jwt for authentication.

- Config (`src/config/settings/`):
  Registers middlewares, exceptions, and JWT logic from core/.

## 🚀 Future Improvements

Add `rate-limiting middleware.`

Add audit logging in `core/db/.`

Create a global caching utility for apps.
