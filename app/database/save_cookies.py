from app.database.connect import MysqlConnect
from app.cookies.cookie_provider import CookieProvider
import json

class SaveCookies:

    def __init__(self):
        self.connection = MysqlConnect()
        self.cookies = CookieProvider()
    

    def save_cookies_in_database(self):
        cookies = self.cookies.get_cookies_from_browser()
        
        if not cookies:
            print("No Cookies Found!")
            return False

        cookies_json = json.dumps(cookies)

        try: 
            query = "INSERT INTO cookies (cookie) VALUES (%s)"
            self.connection.cur.execute(query, (cookies_json,))
            self.connection.db.commit()

            print("Cookies saved successfully.")
            return True
        
        except Exception as e:
            self.connection.db.rollback()
            print("Database error:", e)
            return False

        finally:
            self.connection.cur.close()
            self.connection.db.close()

if __name__ == "__main__":
    a = SaveCookies()
    aa = a.save_cookies_in_database()
    print(aa)