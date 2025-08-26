# Contributing to Django Rwanda

## Welcome

Thank you for your interest in contributing to **Django Rwanda**! 🎉  
This project is a **modular Django system** designed to support the Rwandan Django community. Your contributions help improve functionality, add new features, fix bugs, and enhance the overall quality of the project.

We welcome contributions of all kinds, from code and documentation to testing and design suggestions. Together, we can make **Django Rwanda** a robust and well-organized system for the community.

For an overview of the project structure and layers, please refer to the [README.md](./README.md) file.

---

## How to Contribute

### 1. Fork and Clone

1. Fork the repository on GitHub.
2. Clone your fork locally:

```bash
git clone https://github.com/djangorwanda/Django-Rwanda.git
cd Django-Rwanda
```

3. Set up your development environment:

```bash
# using uv
uv venv
uv sync

# using python with pip
python -m venv env
source env/bin/activate      # Linux/macOS
env\Scripts\activate         # Windows
pip install -r requirements.txt

# run the project
uv run ./src/manage.py runserver
# or 
python ./src/manage.py runserver

```

### 2. Create a Branch

| Type     | Prefix      | Example                        |
|----------|------------|--------------------------------|
| Feature  | feature/   | feature/add-user-registration  |
| Bugfix   | bugfix/    | bugfix/fix-login-error         |
| Hotfix   | hotfix/    | hotfix/security-patch          |


```bash
git checkout -b feature/your-feature-name
```

### 3. Commit Changes

- Write clear and descriptive commit messages.

- Use Conventional Commits: 

```vbnet
feat: add user profile API
fix: correct post serialization
refactor: move shared functions to core/utils.py
docs: update API documentation
```
- Include type hints and follow PEP8 standards.

### 4. Pull Request (PR)

1. Push your branch to your fork:

```bash
Push your branch to your fork:
```

2. Open a Pull Request against the main repository.

3. Link related issues and describe the changes clearly.

4. Maintainers will review your PR and suggest changes if needed.

---

## Code Standards

- Follow PEP8 and Python best practices.

- Use type hints where appropriate.

- Format code with:

    - black for code formatting

    - isort for imports

    - ruff for linting and quality checks

- Place app-specific logic in `src/apps/<app-name>`.

- Place shared infrastructure logic in `src/core/`.

- Follow modular conventions in `src/api/` for API endpoints and routers.

---

## Testing Guidelines

- Tests are located under each app in tests/.

- Run all tests:

```bash
python src/manage.py test
# or if using pytest
pytest
```
- Include tests for:

    - Unit tests for models, serializers, and services

    - Integration tests for API endpoints

    - Functional tests for workflows

- Aim for good coverage, especially for new features.

---

## Documentation Guidelines

- Update documentation in docs/ or README.md for:

    - New app features

    - API changes

    - Deployment or environment updates

- Use clear Markdown formatting and link to relevant sections.

- Document functions, classes, and modules in code using docstrings.

--- 

## Communication & Code of Conduct

- All contributors must follow the [Code of Conduct](./CODE_OF_CONDUCT.md).

- Maintain respectful and professional collaboration.

- Use issues, PRs, and discussion threads for communication.

- Be patient and provide constructive feedback.

## Advanced Contributions

- Adding new apps: Follow the modular structure in `src/apps/`.

- Extending the API layer: Use versioned routers in `src/api/v1/`.

- Adding infrastructure logic: Place reusable utilities in `src/core/`.

- Contribute to `middleware`, security helpers, or database selectors for cross-app functionality.

---

Thank you for helping build and improve Django Rwanda! 🚀
Your contributions strengthen the community and make this project accessible, maintainable, and scalable.

---


