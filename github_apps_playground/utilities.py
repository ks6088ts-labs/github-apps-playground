import logging

from github_apps_playground.settings.common import CommonSettings


def get_logger(
    name: str,
) -> logging.Logger:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(levelname)s:%(name)s:%(message)s"))

    logger = logging.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(level=CommonSettings().common_log_level)

    return logger
