import requests
import json
from app.database.get_cookies import GetCookies
import random

class SessionBuilder:
    def __init__(self):
        self.cookies = GetCookies()
        self.cookie_id = None

    def build_session(self):
        cookies = self.cookies.get_cookies()

        if not cookies:
            print("No Cookies from database to create seession")
            return None
        
        cookies_data = []

        for cookie in cookies:
            cookie_info= {
                "id" : cookie[0],
                "cookie" : cookie[1],
                "counter" : cookie[2]
            }
            cookies_data.append(cookie_info)

        cookie = random.choice(cookies_data)
        self.cookie_id = cookie["id"]
        cookie_data = cookie["cookie"]

        if isinstance(cookie_data, str):
            cookie_data = json.loads(cookie_data)

        session = requests.Session()

        for cookie in cookie_data:
            session.cookies.set(
                name=cookie["name"],
                value=cookie["value"],
                domain=cookie.get("domain"),
                path=cookie.get("path", "/")
            )

        return session