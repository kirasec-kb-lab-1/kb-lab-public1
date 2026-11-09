import os
import sqlite3


def search(db, term):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("SELECT * FROM docs WHERE title='" + term + "'")
    return cur.fetchall()


def archive(target):
    os.system("zip -r /tmp/a.zip " + target)
