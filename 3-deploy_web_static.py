#!/usr/bin/python3
"""
fabric file
"""

import os.path
from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir

env.hosts = ['54.144.152.30', '35.174.176.12']
env.user = 'ubuntu'  # Replace with your SSH username
env.key_filename = '~/.ssh/school'  # Replace with the path to your private key


def do_pack():
    """
    archieve packr
    """
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(current_time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        return None


def do_deploy(archive_path):
    """
    archeieve the web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        #
        put(archive_path, "/tmp/")
        archive_name = os.path.basename(archive_path)
        release_path = "/data/web_static/releases/{}".format(
            archive_name.split('.')[0])

        #
        run("mkdir -p {}".format(release_path))

        #
        run("tar -xzf /tmp/{} -C {}".format(archive_name, release_path))

        #
        run("rm /tmp/{}".format(archive_name))
        run("mv {}/web_static/* {}".format(release_path, release_path))
        run("rm -rf {}/web_static".format(release_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_path))

        print("New version deployed!")
        return True
    except Exception as e:
        return False


def deploy():
    """
    depoly"""
    archive_path = do_pack()
    return archive_path and do_deploy(archive_path)


if __name__ == "__main__":
    deploy()
