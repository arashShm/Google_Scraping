from app.database.connect import MysqlConnect

class GetCookies:
    def __init__(self):
        self.connection = MysqlConnect()

    def get_cookies(self):
        try : 
            query = "SELECT id, cookie, counter FROM cookies ORDER BY counter ASC"
            self.connection.cur.execute(query)
            cookies = self.connection.cur.fetchall()
            return cookies
        
        except Exception as e:
            print("Cookie fetching for session error:", e)
            return None
            
        finally:
            self.connection.cur.close()
            self.connection.db.close()

