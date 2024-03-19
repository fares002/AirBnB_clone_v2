#!/usr/bin/python3
# delete archive.
import os
from fabric.api import *

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_clean(number=0):
    """delete out of date archeives 
    """
    arvnum = 1 if int(number) == 0 else int(number)

    archeive = sorted(os.listdir("versions"))
    [archeive.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archeive]

    with cd("/data/web_static/releases"):
        archeive = run("ls -tr").split()
        archeive = [a for a in archeive if "web_static_" in a]
        [archeive.pop() for i in range(num)]
        [run("rm -rf ./{}".format(a)) for a in archeive]
