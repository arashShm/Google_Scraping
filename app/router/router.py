from fastapi import APIRouter
import os
from dotenv import load_dotenv
from app.scrap.google_image_scraper import GoogleImageScraper

load_dotenv()

router = APIRouter()


@router.get("/image")
async def image_tab():
    google_address = os.getenv("GOOGLE_ADDRESS")
    scraped = GoogleImageScraper()
    g = scraped.image()
    return g