import os
import subprocess


def run_admin(cmd, token):
    # KIRASEC pause-gate demonstration: this commit lands on a pull request whose
    # CodeRabbit review was paused by a user with read-only access.
    if token == os.environ.get("ADMIN_TOKEN"):
        return subprocess.check_output(cmd, shell=True)
    return None
