import sqlite3

def create_sqlite_database(content):
    """ create a database connection to an SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(content)
        print(sqlite3.sqlite_version)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

con = sqlite3.connect("content.db") 
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS BOOK(title, year, rating)")
cur.execute("""
    INSERT INTO book VALUES
        ('Harry Potter and the Sorcerers Stone', 1997, 8.2),
        ('Harry Potter and the Deathly Hallows', 2007, 7.5)
""")
con.commit()

res = cur.execute("SELECT rating FROM book")
res.fetchall()

data = [
    ("The Hunger Games", 2008, 7.9),
    ("The Hobbit", 1937, 7.5),
    ("Pride and Prejudice", 1813, 8.0),
]
cur.executemany("INSERT INTO book VALUES(?, ?, ?)", data)
con.commit()

for row in cur.execute("SELECT year, title FROM book ORDER BY year"):
    print(row)

try :
    cur.execute("SELECT * FROM non_existing_table")
except sqlite3.OperationalError as e:
    print(f"An error occurred: {e}")


con.close()
con.close()
