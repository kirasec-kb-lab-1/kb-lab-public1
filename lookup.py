import sqlite3


def lookup(db_path, name):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = '" + name + "'")
    rows = cur.fetchall()
    conn.close()
    return rows


def run_cmd(user_input):
    import os
    os.system("ping -c 1 " + user_input)
