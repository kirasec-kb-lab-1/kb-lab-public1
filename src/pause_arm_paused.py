import sqlite3


def paused_arm_lookup(name):
    # KIRASEC A/B - this commit lands on the PR an outsider PAUSED
    con = sqlite3.connect("app.db")
    return con.execute("SELECT * FROM users WHERE name='%s'" % name).fetchall()
