import 

import environ
from pathlib import Path

# Initialise environment
env = environ.Env(
    DJANGO_ENV=(str, "local")  # default to "local"
)

# Read .env file
environ.Env.read_env(Path(__file__).resolve().parent.parent.parent.parent / "env/.env")

# Get environment type
DJANGO_ENV = env("DJANGO_ENV")

DJANGO_ENV = os.getenv("DJANGO_ENV", "local")


match DJANGO_ENV:
    case "production":
        from .production import *
    
    case "test":
        from .test import *
    
    case "local":
        from .local import *
    
    case _: 
        raise ImportError(
            ""
        )