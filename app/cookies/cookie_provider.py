import browser_cookie3

class CookieProvider:

    def get_cookies_from_browser(self):
        try: 
            chrome_cookies = browser_cookie3.chrome(
                domain_name=".google.com"
            ) 
            cookies = []

            for cookie in chrome_cookies:
                cookies.append({
                    "name" : cookie.name,
                    "value" : cookie.value,
                    "domain" : cookie.domain,
                    "path" : cookie.path,
                })
                
            return cookies
        
        except Exception as e:
            print("Cookie error:", e)
            return None
