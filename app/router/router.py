from fastapi import APIRouter
import os
from dotenv import load_dotenv
from app.scrap.google_image_scraper import GoogleImageScraper

load_dotenv()

router = APIRouter()


@router.get("/image")
async def get_image_tab(query : str):
    image_tab_html = GoogleImageScraper(query)
    image = image_tab_html.get_google_html_tab()
    return image