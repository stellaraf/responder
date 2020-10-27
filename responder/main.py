"""Application Runner."""

# Standard Library
import shutil

# Third Party
from gunicorn.app.base import Config, BaseApplication

# Project
from responder.config import params
from responder.util.formatters import format_listen_address


class ResponderWSGI(BaseApplication):
    """Custom gunicorn app."""

    def __init__(self, app: BaseApplication, options: Config) -> None:
        """Initialize custom WSGI."""
        self.application = app
        self.options = options or {}
        super().__init__()

    def load_config(self) -> None:
        """Load gunicorn config."""
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }

        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self) -> BaseApplication:
        """Load gunicorn app."""
        return self.application


def start(**kwargs: Config) -> None:
    """Start app via gunicorn."""

    ResponderWSGI(
        app="responder.api:api",
        options={
            "worker_class": "uvicorn.workers.UvicornWorker",
            "preload": True,
            "keepalive": 10,
            "command": shutil.which("gunicorn"),
            "bind": ":".join(
                (format_listen_address(params.listen_address), str(params.listen_port))
            ),
            "workers": params.workers,
            **kwargs,
        },
    ).run()


if __name__ == "__main__":
    start()
