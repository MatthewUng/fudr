import sqlite3

def main():
    db = sqlite3.connect('database.sqlite3')
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS groups (id integer primary key, name text)""")
    cursor.execute("""INSERT INTO groups (id, name) VALUES (NULL, "first");""")
    cursor.execute("""INSERT INTO groups (id, name) VALUES (NULL, "second");""")

if __name__ == "__main__":
    main()