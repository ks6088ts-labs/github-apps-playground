from fastapi import FastAPI

from github_apps_playground.routers.common import router as common_router

app = FastAPI(
    docs_url="/",
)

for router in [
    common_router,
    # Add routers here
]:
    app.include_router(router)
