import os
import requests

class GoogleImageScraper:
    def __init__(self, query : str):
        self.google_address = os.getenv("GOOGLE_ADDRESS")
        self.query = query

    def get_google_html_tab(self):
        params = {
            "q" : self.query,
            "tbm" : "isch"
        }
        response = requests.get(self.google_address , params=params)
        response.raise_for_status()

        return response.text