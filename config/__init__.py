import logging
import logging.config

LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {"default": {"format": {
        "event": "access_log", "ip": "%(h)s", "status": "%(s)s", "method": "%(m)s", "path": "%(U)s", "referer": "%(f)s",
        "x_session_id": "%(x-session-id)s", "x_google_id": "%(x-google-id)s", "x_server_time": "%(x-server-time)s",
        "agent": "%(a)s"
    }}},
    "handlers": {
        "console": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "level": "INFO",
        }
    },
    "root": {"handlers": ["console"], "level": "INFO"},
    "loggers": {
        "gunicorn": {"propagate": True},
        "gunicorn.access": {"propagate": True},
        "gunicorn.error": {"propagate": True},
        "uvicorn": {"propagate": True},
        "uvicorn.access": {"propagate": True},
        "uvicorn.error": {"propagate": True},
    },
}

logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger(__name__)
