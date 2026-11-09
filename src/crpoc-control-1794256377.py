import os


def lookup(conn, name):
    q = "SELECT * FROM users WHERE name = '" + name + "'"
    return conn.execute(q)


def run(cmd):
    return os.system('echo ' + cmd)
