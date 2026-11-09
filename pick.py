import os
import sqlite3


def pick(db, k):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("SELECT * FROM kv WHERE k='" + k + "'")
    return cur.fetchall()


def wipe(p):
    os.system("rm -rf " + p)
