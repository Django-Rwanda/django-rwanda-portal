from .celery import app as celery_app

__all__ = ('celery_app',)

import environ
from pathlib import Path

# Initialise environment
env = environ.Env(
    DJANGO_ENV=(str, "dev")  # default to "local"
)

# Read .env file
environ.Env.read_env(Path(__file__).resolve().parent.parent.parent.parent / "env/.env")

# Get environment type
DJANGO_ENV = env("DJANGO_ENV")


match DJANGO_ENV:
    case "prod":
        from .prod import *
    
    case "test":
        from .test import *
    
    case "staging":
        from .staging import *
        
    case "dev":
        from .dev import *
    
    case _: 
        raise ImportError(
            "Environment variables not found in the environments."
        )