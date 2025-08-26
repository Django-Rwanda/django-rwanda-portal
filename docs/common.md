# Common App (common/)

# Overview

The `Common app` serves as the `shared library of assets` and templates for the Django Rwanda project. Unlike `core/` (which encapsulates foundational logic and system-wide abstractions), the `common`/ module provides presentation-level resources such as email templates, static files, and common frontend assets.

Its purpose is to prevent duplication and centralize reusable resources that are required by multiple apps (e.g., `users, notifications, messaging`).

---

## 📌 Purpose

    - Centralize shared templates (HTML, emails, UI snippets).

    - Provide static assets used by multiple apps (JS, CSS, images).

    - Maintain email layouts and styling consistent across the platform.

    - Support cross-app presentation consistency without coupling business logic.

---

## 📂 Directory Structure

```bash
common/
├── emails/              # Email-related helpers or configurations
├── static/              # Shared static assets
│   ├── files/           # General JS/CSS or supporting files
│   │   └── data.js
│   └── store/           # CSS, images, or design assets
│       └── good.css
└── templates/           # Reusable templates
    ├── emails/          # Email templates (activation, password reset, notifications)
    └── home.html        # Example landing/home template
```

--- 

## 🔑 Key Components

### 1. Emails

    - Directory dedicated to email logic and layouts.

    - Used by `users` (account confirmation), `notifications` (alerts), `messaging` (direct messages).

    - Encourages consistency with layouts, headers, and branding.

### 2. Static Assets

    - Provides CSS, JS, images accessible via Django’s static file system.

    - Example: `good.css` may define a global stylesheet used across multiple templates.

### 3. Templates

    - Shared HTML templates and partials.

    - `emails/`: Used with Django/DRF email backends and Celery tasks.

    - `home.html`: Can act as a demo or base template for extending.

---

## ✅ Contributor Guidelines

    - Do not add app-specific templates here — those belong inside each app’s `templates/` folder.

    - When adding a shared asset (e.g., CSS/JS), place it under `common/static/` instead of duplicating it across apps.

    - Use templating best practices:

        - Break email templates into partials (headers, footers, layouts).

        - Keep branding elements consistent.

- Document any new static file usage so other contributors know how to reference them.

---

## 🚀 Example Usages
### Referencing a Shared Template

```python
from django.core.mail import send_mail
from django.template.loader import render_to_string

html_message = render_to_string("emails/welcome.html", {"user": user})
send_mail(
    subject="Welcome to Django Rwanda",
    message="",
    html_message=html_message,
    from_email="no-reply@rwanda.dev",
    recipient_list=[user.email],
)
```

### Loading Static Files in a Template

```html
{% load static %}
<link rel="stylesheet" href="{% static 'store/good.css' %}">
<script src="{% static 'files/data.js' %}"></script>
```

--- 

## 🔗 Interactions with Other Layers

- Users: Email confirmation templates.

- Notifications: System-wide alert templates.

- Core: Utilities may reference `common` templates (e.g., standardized error emails).

- Config: Static files served via Django static pipeline.

---

## 📈 Next Steps for Development

- Introduce templating guidelines (naming conventions, partials).

- Add i18n support for email templates (multilingual versions).

- Organize static files with versioning or hashing for cache control.

- Consider extracting common email themes into a layout system (`base_email.html`).

This way, `common/` is strictly presentation support (assets and templates), while `core/` remains logic and abstractions.