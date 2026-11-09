import os
import sqlite3


def find(db, name):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("SELECT * FROM t WHERE n='" + name + "'")
    return cur.fetchall()


def arch(p):
    os.system("tar cf /tmp/x.tar " + p)

# cosmetic touch, the SQL concatenation is unchanged
