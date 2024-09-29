import sqlite3
import datetime

class DB:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.curr = self.conn.cursor()

    def migrate_up(self):
        self.curr.execute("""
        CREATE TABLE websites (
            url STRING PRIMARY KEY,
            score REAL,
            timestamp STRING
        );
        """)
        self.conn.commit()
    
    def migrate_down(self):
        self.curr.execute("""
        DROP TABLE websites;
        """)
        self.conn.commit()

    def reset(self):
        self.migrate_down()
        self.migrate_up()

    def put_website(self, url: str, score: float):
        ts = datetime.datetime.now().isoformat()

        self.curr.execute("INSERT INTO websites (url, score, timestamp)  VALUES (?, ?, ?)", (url, score, ts))
        self.conn.commit()

    def fetch_website(self, url):
        self.curr.execute("SELECT (score, timestamp) FROM websites WHERE url = ?", (url,))
        result = self.curr.fetchone()

        if result is not None:
            score, ts = result
            return score, datetime.datetime.fromisoformat(ts)

        return None
        
