"""Application Configuration from Type-Safe Environment Variables."""

# Third Party
from pydantic import BaseSettings


class Params(BaseSettings):
    """Global App Configuration Parameters."""

    listen_address: str = "0.0.0.0"
    listen_port: int = 8080
    workers: int = 4
