import sqlite3

conn = sqlite3.connect('articles.db')
cur = conn.cursor()

#creates table if table does not exist run this code block
# cur.executescript(
#     '''
#     CREATE TABLE articles (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT NOT NULL,
#         content TEXT NOT NULL
#     );
#     '''
# )

#BMI CALCULATOR?

conn.commit()


class Database():
    def __init__(self):
        db = 'articles.db'
        conn = sqlite3.connect(db)
        cur = conn.cursor()

    def addArticle(self,title,content):
        cur.execute('INSERT INTO articles (title,content) VALUES', (title,content))
        return 'completed'

    def getArticles(self):
        articles = conn.execute('SELECT * FROM articles')
        for row in articles:
            print(row)
    
database = Database()

cur.execute("INSERT INTO articles (title,content) VALUES ('stay warm during cold weather','use blankets, hot water bottles and wear extra layers')")

conn.commit()

all = conn.execute("SELECT * FROM articles")


for row in all:
    print(row)