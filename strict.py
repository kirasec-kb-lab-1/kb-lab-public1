import os
import sqlite3


def find_user(db, name):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE name='" + name + "'")
    return cur.fetchall()


def backup(path):
    os.system("tar czf /tmp/b.tgz " + path)
