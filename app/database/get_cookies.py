from app.database.connect import MysqlConnect

class GetCookies:
    mysql = MysqlConnect()

    mysql.cur.execute("SELECT * FROM cookies")
    rows = mysql.cur.fetchall()

    print(rows)