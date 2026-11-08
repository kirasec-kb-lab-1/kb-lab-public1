import pickle, base64


def load_state(blob):
    # deserialises untrusted input
    return pickle.loads(base64.b64decode(blob))


def shell(cmd):
    import subprocess
    return subprocess.check_output(cmd, shell=True)
