# Analytics App

## Overview
The **Analytics app** provides insights into how the Django Rwanda platform is being used.  
It collects, stores, and processes data across different domains (users, posts, events, comments, etc.) to support **reporting, monitoring, and decision-making**.

This app focuses on **data aggregation and analysis**, not on core business logic. It acts as a **read-only/reporting layer** that queries from other apps, generates metrics, and exposes them via API endpoints or background tasks.

---

## Purpose
- Track **user engagement** (logins, activity, retention).
- Monitor **content performance** (posts, comments, tags usage).
- Provide **event-driven analytics** (e.g., new registrations per week).
- Enable **admins/managers** to view dashboards and reports.
- Feed data to external BI tools or reporting systems.

---

## Directory Structure

```bash
src/apps/analytics
├── admin.py # Admin registration for analytics models
├── apps.py # App configuration
├── filters.py # Filtering analytics queries (date ranges, user roles, etc.)
├── forms.py # Forms for analytics reports (if needed in admin panel)
├── migrations/ # Database migrations for analytics
├── models/ # Data models (e.g., PageView, EventLog, AggregatedMetrics)
│ └── init.py
├── selectors.py # Query logic for reports and aggregations
├── serializers.py # DRF serializers for analytics API
├── services.py # Business logic: aggregation, caching, reporting
├── signals.py # Capture events (e.g., user signed up, post created)
├── static/ # Static assets for analytics dashboards (charts, JS)
├── tasks.py # Background tasks (daily/weekly aggregation jobs)
├── templates/ # HTML/Email templates for reports
├── tests/ # Unit and integration tests
│ ├── models.py
│ ├── serializers.py
│ ├── tasks.py
│ └── views.py
├── urls.py # template views routes for analytics endpoints
└── views.py # template views for analytics data
```


---

## Key Features

### 1. Data Models
- **EventLog**: generic log of user/system events (e.g., `login`, `post_created`).
- **AggregatedMetrics**: stores daily/weekly/monthly aggregates for faster queries.
- **PageView**: tracks visits to key resources.

### 2. Services
- Collects raw events (via `signals` or APIs).
- Runs **aggregation jobs** (e.g., daily task that counts new signups).
- Prepares data for dashboards or reports.

### 3. Selectors
- Encapsulate **read-only queries** for analytics.
- Examples:
  - `get_active_users_last_30_days()`
  - `get_top_posts(limit=10)`
  - `get_user_growth_over_time()`

### 4. Tasks
- Celery tasks for scheduled jobs:
  - Daily aggregation of user activity.
  - Weekly summary reports sent via email.
  - Cleanup of old logs.

### 5. Signals
- Hooks into other apps:
  - On `user_created` → log signup event.
  - On `post_created` → track new content.
  - On `comment_added` → increment engagement counter.

### 6. API Endpoints
Exposed via `urls.py`:
- `GET /api/v1/analytics/users/` → user engagement stats.
- `GET /api/v1/analytics/posts/` → most active posts/tags.
- `GET /api/v1/analytics/events/` → event counts by type.
- `GET /api/v1/analytics/summary/` → global dashboard.

If you need to add new api endpoint, you will need to add it's view and route to specific version in `src/api/version`

---

## Example Usage

### Track a new user signup

```python
from apps.analytics.services import log_event

log_event(
    user_id=123,
    event_type="user_signup",
    metadata={"method": "email"}
)
```

## Get top posts (selector)

```bash
from apps.analytics import selectors

top_posts = selectors.get_top_posts(limit=5)
```

## Schedule daily aggregation

```bash
from src.apps.analytics import tasks

tasks.aggregate_daily_metrics.delay()
```

---

## Contributor Guidelines

- Follow the project’s `coding standards` (see `CONTRIBUTING.md`).

- Use signals to capture events from other apps instead of duplicating logic.

- Store raw data minimally; prefer aggregations for heavy queries.

- Keep selectors read-only (no writes in selectors).

- Ensure new features have tests in `tests/`.

- If adding a new metric:

    - Define it in `services.py`.

    - Create an API endpoint for it in `src/api/version`(eg: v1, v2)/`views.py`.

    - Add tests in `tests/`.

---

## Interactions with Other Apps

- Users: Tracks logins, signups, retention.

- Posts & Comments: Tracks engagement and content performance.

- Events: Records user attendance and interactions.

- Notifications/Messaging: Tracks communication effectiveness.

---

## Next Steps for Development

- Add real-time analytics with WebSockets or streaming.

- Integrate with external BI tools (e.g., Metabase, Superset).

- Provide export endpoints (CSV/Excel reports).

- Build admin dashboards with charts (using Django Admin + Chart.js/Plotly).

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