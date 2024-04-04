#!/usr/bin/python3
# fabfile.
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["54.144.152.30", "35.174.176.12"]


def do_deploy(archive_path):
    """
    archeive distrbuting to web server
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    splt = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(splt)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(splt)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, splt)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(splt, splt)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(splt)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(splt)).failed is True:
        return False
    return True
