import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def get_env(name: str, default: str | None = None) -> str | None:
    return os.getenv(name, default)


def get_app_config() -> dict:
    return {
        "base_dir": str(BASE_DIR),
        "environment": get_env("ENVIRONMENT", "development"),
        "api_base_url": get_env("API_BASE_URL", "https://jsonplaceholder.typicode.com"),
    }
