from fastapi import APIRouter

from github_apps_playground.settings.common import CommonSettings
from github_apps_playground.utilities import get_logger

settings = CommonSettings()
logger = get_logger(name=__name__)

router = APIRouter(
    prefix="/common",
    tags=["common"],
)


@router.get("/info")
def info():
    logger.info(settings.json(indent=2))
    return {
        "version": settings.common_version,
    }
