rwanda-community/
├─ pyproject.toml                 # dependencies, linters, type checkers
├─ README.md                      # overview, setup instructions
├─ CONTRIBUTING.md                # how contributors should work
├─ CODE_OF_CONDUCT.md
├─ LICENSE
├─ Makefile                       # dev commands
├─ .editorconfig
├─ .gitignore
├─ .pre-commit-config.yaml
├─ .github/
│  └─ workflows/ci.yml            # CI: tests, lint, coverage
├─ docs/                           # docs & architecture diagrams
│  ├─ adr/
│  └─ development.md
├─ env/                            # environment variables
│  ├─ .env.example
├─ scripts/                        # helpers: seed, format, wait for DB
├─ docker/                         # Docker files
├─ infra/                          # infra, Kubernetes, Terraform
├─ tests/                           # global tests (unit, integration, e2e)
└─ src/
   ├─ manage.py
   ├─ config/
   │  ├─ __init__.py
   │  ├─ asgi.py
   │  ├─ wsgi.py
   │  ├─ urls.py
   │  └─ settings/
   │     ├─ __init__.py
   │     ├─ base.py
   │     ├─ local.py
   │     ├─ test.py
   │     └─ production.py
   ├─ core/                        # shared utilities (db, auth, middleware)
   ├─ common/                      # templates, static, emails, notifications
   
   ├─ api/                         # API versioning (v1, v2)
   └─ apps/                        # domain apps
       ├─ users/                   # registration, login, profiles
       ├─ posts/                   # user posts, articles, discussions
       ├─ events/                  # community events, RSVPs
       ├─ notifications/           # in-app and email notifications
       ├─ comments/                # comments for posts/events
       ├─ tags/                    # categorization system
       └─ analytics/               # community insights, stats
