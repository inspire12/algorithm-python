import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname).1s | %(asctime)s | %(name)s | %(message)s",
)
log = logging.getLogger("app")

