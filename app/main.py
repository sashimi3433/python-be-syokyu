import os
from fastapi import FastAPI
from .routers import item_router, list_router

DEBUG = os.environ.get("DEBUG", "") == "true"

app = FastAPI(
    title="Python Backend Stations",
    debug=DEBUG,
)

if DEBUG:
    from debug_toolbar.middleware import DebugToolbarMiddleware
    app.add_middleware(
        DebugToolbarMiddleware,
        panels=["app.database.SQLAlchemyPanel"],
    )

@app.get("/health")
def get_health():
    return {"status": "ok"}

app.include_router(list_router.router)
app.include_router(item_router.router)