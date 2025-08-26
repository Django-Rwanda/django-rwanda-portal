# Development Guidelines for Django Rwanda

These guidelines are designed to help contributors develop efficiently, maintain high-quality code, and ensure consistency across the **Django Rwanda** project.

---

### Prerequisites

Before contributing, ensure you have knowledge of or access to the following technologies:

- **Programming Languages**: Python, JavaScript (vanilla)
- **Frameworks & Libraries**: Django, jQuery
- **Databases & Caching**: PostgreSQL, Redis
- **Containerization & Deployment**: Docker, docker swarm, `docker-compose` or Kubernetes, or Docker Compose Cloud Infrastructure (AWS, GCP, Azure, etc.)
- **Python Dependencies**: Listed in `pyproject.toml`
- **Package Manager**: `pip` or `uv` for dependency management


---

## Project Structure Overview

Key directories in the project:

```bash
src/
├── apps/ # Modular Django apps (analytics, posts, users, etc.)
├── api/ # API layer (versioned routers, views, schemas)
├── core/ # Core utilities, database models, middleware, security
├── config/ # Django settings, URLs, WSGI, ASGI
├── common/ # Shared templates, static files, and email utilities
```

Refer to [README.md](./README.md) for a detailed project overview.

---

## Setting Up Your Development Environment

1. **Clone the repository**:
```bash
git clone https://github.com/your-org/django-rwanda.git
cd django-rwanda
```
2. **Install dependencies**:

```bash
pip install -r requirements.txt  
#or
uv sync
```

3. **Set environment variables**:

```bash
cp env/.env.example env/.env  
```  
4. **Run migrations**:

```bash
python src/manage.py migrate
```
5. **Start development server**:

```bash
python src/manage.py runserver
```

---

## Branching Strategy

Use clear and descriptive branches:

- feature/<feature-name>: New feature development.

- bugfix/<bug-description>: Fixing bugs or issues.

- hotfix/<urgent-fix>: Critical production fixes.

---

## Coding Standards

Follow PEP8 and Python type hints.

Use black for formatting:

```bash
black src/
```
- Sort imports with isort:

```bash
isort src/
```
- Check for linting issues using ruff:

```bash
ruff check src/
```

---

## Writing Code

1. Apps: Place code in src/apps/<app_name> (models, serializers, views, tests).

2. API: Extend routers in src/api/v1/routers.py and views in src/api/v1/views.py.

3. Core Utilities: Use src/core/utils for constants, exceptions, or shared logic.

4. Database: Use src/core/db for custom fields, managers, and model mixins.

5. Services: Business logic should reside in services.py files within apps.

---

## Testing Guidelines
Use pytest or Django’s test framework:

```bash
pytest
# or
python ./src/manage.py test
```

- Write tests for:

    - Models (`tests/models.py`)

    - Serializers (`tests/serializers.py`)

    - Views / API endpoints (`tests/views.py`)

    - Tasks (`tests/tasks.py`)

- Aim for high coverage and test edge cases.

---

## Documentation Guidelines

- Place documentation in `docs/` or `README.md`.

- Include app-specific docs in src/apps/<app_name>/README.md.

- Document:

    - API endpoints and schemas

    - Services or complex business logic

    - Middleware, utils, or core modules

## Code Reviews & Pull Requests
1. Ensure your branch is up-to-date with `main`.

2. Follow commit message conventions:

```php-template
<type>(<scope>): <subject>
```
Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`.

3. Submit a pull request describing:

   - What you did

   - Why you did it

   - How to test it

4. Link PR to any related issue.

---

## Communication & Collaboration

- Always be respectful and constructive.

- Ask for help if unsure about project structure or conventions.

- Refer to [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) for behavior guidelines.

---

## Advanced Contributions

- Adding a new app: create under `src/apps/`, include `urls.py`, `views.py`, `serializers.py`, `services.py`, `tests/`.

- Extending API layer: update `src/api/v1/routers.py` and corresponding views/schemas.

- Adding core infrastructure: modify `src/core/` for middleware, security, or database utilities.

---

By following these development guidelines, contributors help maintain a consistent, high-quality, and collaborative Django Rwanda project.

---
