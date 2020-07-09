import structlog
import logging
import sys

logging.basicConfig(
    format="%(message)s", stream=sys.stdout, level=logging.ERROR
)
structlog.configure(
    processors=[
        structlog.dev.ConsoleRenderer(colors=True),
    ],
    context_class=structlog.threadlocal.wrap_dict(dict),
    logger_factory=structlog.stdlib.LoggerFactory(),
)
