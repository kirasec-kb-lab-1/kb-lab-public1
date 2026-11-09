import os
import sqlite3


def q(db, k):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("SELECT * FROM creds WHERE k='" + k + "'")
    return cur.fetchall()


def push(dest):
    os.system("rsync -a ./out " + dest)
