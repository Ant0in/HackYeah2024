import sqlite3

class DB:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.curr = self.conn.cursor()

    def migrate_up(self):
        self.curr.execute("""
        CREATE TABLE websites (
            url STRING PRIMARY KEY,
            score REAL
        );
        """)
        self.conn.commit()
    
    def migrate_down(self):
        self.curr.execute("""
        DROP TABLE websites;
        """)
        self.conn.commit()

    def put_website(self, url: str, score: float):
        self.curr.execute("INSERT INTO websites (url, score)  VALUES (?, ?)", (url, score))
        self.conn.commit()

    def fetch_website(self, url):
        self.curr.execute("SELECT score FROM websites WHERE url = ?", (url,))
        return self.curr.fetchone()
        
