from fastapi import FastAPI
from app.router.router import router


app = FastAPI(
    title="Google Scraper API",
    version="1.0.0"
)

app.include_router(router)