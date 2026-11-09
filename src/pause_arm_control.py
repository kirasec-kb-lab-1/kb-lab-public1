import sqlite3


def control_arm_lookup(name):
    # KIRASEC A/B - this commit lands on a PR that was NOT paused
    con = sqlite3.connect("app.db")
    return con.execute("SELECT * FROM users WHERE name='%s'" % name).fetchall()
