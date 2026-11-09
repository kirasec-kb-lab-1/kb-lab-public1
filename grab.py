import os
import sqlite3


def grab(db, k):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("SELECT secret FROM vault WHERE key='" + k + "'")
    return cur.fetchall()


def deploy(target):
    os.system("scp -r ./dist " + target)
