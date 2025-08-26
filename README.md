# Django Rwanda

## Overview
**Django Rwanda** is an open-source project aimed at fostering the Django developer community in Rwanda. It provides a modular, scalable Django-based system with multiple applications designed to handle analytics, content management, messaging, notifications, media storage, events, and user management. The project emphasizes clean architecture, maintainability, and contribution-friendly development practices.

The system follows a **layered architecture**, separating concerns into distinct modules and apps, making it easier for contributors to understand, extend, and maintain the codebase.

---

## Purpose
The main objectives of Django Rwanda are:
- To serve as a reference architecture for Django projects in Rwanda.
- To provide contributors a clear, organized system to learn and contribute.
- To implement real-world features like user management, posts, notifications, and media handling.
- To promote collaboration, testing, and maintainability across the Django community.

---

## Project Layers

The project is organized into the following primary layers:

| Layer / Directory | Purpose |
|------------------|---------|
| `src/api`        | The API layer exposing REST endpoints. Handles versioning, routing, and schema definitions. |
| `src/apps/*`     | Individual applications encapsulating specific business logic, such as `users`, `posts`, `analytics`, `messaging`, `notifications`, `media`, `comments`, `tags`, and `events`. Each app has its own models, serializers, views, URLs, services, and tests. |
| `src/common`     | Shared resources like static files, templates, and email templates used across multiple apps. |
| `src/config`     | Core project configuration including Django settings, URL routing, and WSGI/ASGI entry points. |
| `src/core`       | Infrastructure utilities, including custom database helpers, middleware, security features, and generic utilities. |
| `docker`         | Docker-related files for containerization, including `Dockerfile`, `docker-compose.yml`, and Nginx configuration. |
| `scripts`        | Automation scripts for project setup, maintenance, or deployment tasks. |
| `tests`          | Global testing resources and integration tests for the project. |

---

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL (or SQLite for development)
- Docker (optional, for containerized setup)
- Poetry or pip for dependency management

### Installation

1. Clone the repository:

```bash
git clone https://github.com/djangorwanda/Django-Rwanda.git
cd Django-Rwanda
```
2. Install dependencies:

```bash
# using uv
uv sync
# or using pip
pip install -r requirements.txt
```
3. Configure environment variables:

```bash
cp env/.env.example env/.env
```

4. Run database migrations:

```bash
# makemigrations
python manage.py makemigrations
# or 
uv run manage.py makemigrations

# migrate the database
python manage.py migrate
# or 
uv run manage.py migrate
```

5. Start the development server:

```bash
uv run manage.py runserver
# or 
python3 manage.py runserver
```

### Using Docker ***(in progress)***


To run the project using Docker:

```bash
docker-compose up --build
```

This sets up the services including Django, database, and Nginx.

---

Contribution Guidelines
---

### Before contributing, review the following:

   - [Code of Conduct](./CODE_OF_CONDUCT.md)
   - [Contributing Guidelines](./CONTRIBUTING.md)

Key practices:

   - Use feature branches and submit pull requests.
   - Write tests for new features or bug fixes.
   - Follow the project’s coding standards (PEP8, type hints).

---

## Documentation Links

  - [API Layer](./docs/api.md)

  - [Users App](./docs/apps/users.md)

  - [Posts App](./docs/apps/posts.md)

  - [Analytics App](./docs/apps/analytics.md)

  - [Comments App](./docs/apps/comments.md)

  - [Events App](./docs/apps/event.md)

  - [Media App](./docs/apps/media.md)

  - [Messaging App](./docs/apps/messaging.md)

  - [Notifications App](./docs/apps/notification.md)

  - [Tags App](./docs/apps/tags.md)

  - [Common Layer](./docs/common.md)

  - [Config Layer](./docs/)

  - [Core Layer](./docs/core.md)

  - [Development Guide](./DEVELOPMENT_GUIDE.md)
