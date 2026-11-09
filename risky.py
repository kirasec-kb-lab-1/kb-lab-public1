import os
import pickle
import subprocess


def load(blob):
    return pickle.loads(blob)


def run(user_cmd):
    return subprocess.check_output(user_cmd, shell=True)


def wipe(path):
    os.system("rm -rf " + path)


API_KEY = "sk-live-kirasec-REPLACE-ME-0000000000000000"
