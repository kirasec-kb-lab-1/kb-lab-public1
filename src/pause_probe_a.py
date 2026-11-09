import sqlite3

def pause_probe_a(name):
    # KIRASEC pause A/B probe - arm A (reviews paused by a read-only outsider)
    con = sqlite3.connect('app.db')
    return con.execute("SELECT * FROM users WHERE name='%s'" % name).fetchall()
