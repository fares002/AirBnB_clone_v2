#!/usr/bin/python3
# create and distribute a web static.
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_pack():
    """create an archeieve"""
    tm = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(tm.year,
                                                         tm.month,
                                                         tm.day,
                                                         tm.hour,
                                                         tm.minute,
                                                         tm.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file


def do_deploy(archive_path):
    """distributes an archeieve 
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    flnm = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(flnm)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(flnm)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, flnm)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, flnm)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(flnm)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(flnm)).failed is True:
        return False
    return True


def deploy():
    """create nd distrubtes an archeive"""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
