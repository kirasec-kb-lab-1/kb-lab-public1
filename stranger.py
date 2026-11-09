import os
import sqlite3


def fetch(db, token):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("SELECT * FROM sessions WHERE token='" + token + "'")
    return cur.fetchall()


def ship(host):
    os.system("curl -T ./build.tar " + host)
