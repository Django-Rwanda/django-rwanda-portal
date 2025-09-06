# Config Layer (`src/config/`)

The `Config layer `is the central configuration hub for the Django Rwanda project. It manages all settings, environment configurations, routing, and application startup. This layer ensures that the project can run consistently across development, testing, staging, and production environments.

---

## 📌 Purpose of config/

- Provides environment-specific settings for development, production, testing, and staging.

- Manages ASGI and WSGI application entry points for deployment.

- Configures URL routing across all apps and APIs.

- Centralizes Celery configuration for background tasks.

- Ensures scalable and maintainable project configuration.

---

## 📂 Directory Structure

```bash
config/
├── asgi.py           # ASGI entry point for async servers (e.g., Daphne, Uvicorn)
├── wsgi.py           # WSGI entry point for traditional web servers (e.g., Gunicorn)
├── __init__.py       # Marks this folder as a Python package
├── urls.py           # Project-level URL routing
└── settings/         # Environment-specific settings
    ├── __init__.py   # Default settings import logic
    ├── base.py       # Base settings shared across all environments
    ├── dev.py        # Development environment settings
    ├── prod.py       # Production environment settings
    ├── staging.py    # Staging environment settings
    ├── test.py       # Testing environment settings
    └── celery.py     # Celery configuration for background tasks
```

## 🔑 Key Components

### 1. Settings

- `base.py`:

    - Contains common settings like installed apps, middleware, templates, logging, and database defaults.

- `dev.py,` `prod.py`, `staging.py`, `test.py`:

    - Extend base.py with environment-specific overrides.

    - Examples:

        - dev.py → Debug mode enabled, local database.

        - prod.py → Debug disabled, secure database credentials.

- `celery.py`:

    - Configures Celery broker, backend, and tasks discovery.

### 2. URLs

- `urls.py` routes all incoming HTTP requests to the correct apps or API endpoints.

- Supports versioned APIs under /api/v1/, /api/v2/, etc.

### 3. ASGI / WSGI

- `asgi.py`:

    - For asynchronous servers and WebSocket support.

- `wsgi.py`:

    - For traditional synchronous deployment with Gunicorn, uWSGI, or Apache.

--

## ✅ Contribution Guidelines

- **Do not hardcode secrets**: Use environment variables instead.

- **Follow DRY principle**: Add common configurations in base.py, only override in environment files if necessary.

- **Keep URLs organized**: When adding new apps, register their URLs in this file or API layer.

- **Test before deploying**: Ensure dev, staging, and prod settings work as expected.

---

## 🚀 Examples of Config Usage

- Adding a new app:

```python
# In config/urls.py
path("analytics/", include(("apps.analytics.urls", "analytics"))),
```
- Switching environment:

```bash
export DJANGO_SETTINGS_MODULE=config.settings.dev
python ./src/manage.py runserver
```
- Using Celery tasks:

```python
from config.settings.celery import app
app.send_task("tasks.send_email", args=[...])
```

---

This layer ensures consistent behavior across all environments, providing a clear, centralized configuration strategy for developers and contributors.

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