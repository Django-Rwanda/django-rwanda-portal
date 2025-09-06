# Django Rwanda Portal

# Overview

**Django Rwanda Portal** is an open-source project designed to foster collaboration and knowledge sharing within the Django community in Rwanda. It provides a modular and **scalable system** built with Django, structured into reusable applications and layers for clean architecture, maintainability, and community-driven contributions.

The system emphasizes:

- **Layered architecture** for separation of concerns.

- **Reusability & DRY principles.**

- **Community collaboration** through well-documented code and contribution guidelines.

---

## Purpose

- Serve as a **reference architecture** for Django projects in Rwanda.

- Provide contributors a structured and organized system to learn from and extend.

- Implement real-world features like **user management, posts, notifications, messaging, events, and media handling**.

- Encourage collaboration, testing, and maintainability within the Django community.

---

## Project Structure

The project is organized into the following primary layers:

| **Layer / Directory** | **Purpose** |
|------------------------|-------------|
| **src/api** | API layer exposing versioned REST endpoints (`v1/`). Handles routing and schema definitions. |
| **src/apps/*** | Domain-specific applications (`users`, `posts`, `analytics`, `messaging`, `notifications`, `media`, `comments`, `tags`, `events`). Each app includes its own models, serializers, views, services, tests, etc. |
| **src/common** | Shared templates, static files, and reusable email templates. |
| **src/config** | Django project configuration (settings for `dev`, `prod`, `staging`, `test`), URL routing, WSGI/ASGI entry points, and Celery integration. |
| **src/core** | Core infrastructure utilities: database mixins, middleware, security helpers, constants, and exceptions. |
| **docker/** | Docker setup with `Dockerfile`, `docker-compose.yml`, and Nginx configuration. |
| **infra/** | Infrastructure-related configuration (future use for deployments). |
| **scripts/** | Automation scripts for project setup and maintenance. |
| **docs/** | Documentation for apps, layers, and developer guides. |


---

## Getting Started

## Prerequisites

Before contributing or running the project, ensure you have knowledge of or access to:

- Programming Languages: Python, JavaScript (vanilla)

- Frameworks & Libraries: Django, jQuery

- Databases & Caching: PostgreSQL, Redis

- Containerization & Deployment: Docker, docker-compose (Kubernetes or cloud providers like AWS/GCP/Azure optional)

- Python Dependencies: Defined in pyproject.toml and requirements.txt

- Package Managers: pip or [uv](https://docs.astral.sh/uv/)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/django-rwanda/django-rwanda-portal.git
cd django-rwanda-portal
```

---

## Install dependencies:

```bash
# using uv
uv sync

# or using pip
pip install -r requirements.txt
```

---

## Configure environment variables:

```bash
cp env/.env.example env/.env
```

Run migrations:

```bash
python src/manage.py makemigrations
python src/manage.py migrate
```

---

## Start the development server:

```bash
python src/manage.py runserver
```

---

## Using Docker (Optional)

To run the project with Docker:

```bash
docker-compose up --build
```

This sets up Django, PostgreSQL, and Nginx services.

---

## Contribution Guidelines

Before contributing, review:

- [Code of Conduct](./CODE_OF_CONDUCT.md)

- [Contributing Guidelines](./CONTRIBUTING.md)

Key practices:

- Work on feature branches, submit pull requests.

- Write tests for new features and bug fixes.

- Follow project coding standards (PEP8, type hints).

- Update documentation when introducing new modules or features.

---

## Documentation

- [API Layer](./docs/api.md)

-  **Apps – includes**:

    - [Users](./docs/apps/users.md)

    - [Posts](./docs/apps/posts.md)

    - [Analytics](./docs/apps/analytics.md)

    - [Comments](./docs/apps/comments.md)

    - [Events](./docs/apps/event.md)

    - [Media](./docs/apps/media.md)

    - [Messaging](./docs/apps/messaging.md)

    - [Notifications](./docs/apps/notification.md)

    - [Tags](./docs/apps/tags.md)

- [Common Layer](./docs/common.md)

- [Config Layer](./docs/config.md)

- [Core Layer](./docs/core.md)

- [Development Guide](./DEVELOPMENT_GUIDE.md)

---

## License

This project is licensed under the [MIT License](./LICENSE)

### Copyright (c) 2025 I. Fils