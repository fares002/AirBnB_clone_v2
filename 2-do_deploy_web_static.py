#!/usr/bin/python3
from fabric.api import env, put, run, local
import os


env.hosts = ['54.152.134.222', '35.168.2.251']
env.user = 'ubuntu'

def do_deploy(archive_path):
"""
deploy the archive to the web server
"""
    if not os.path.exists(archive_path):
           print("Error: Archive file {} does not exist.".format(archive_path))
           return False
       
    filename = os.path.basename(archive_path)
    folder_name = filename.split('.')[0]
    release_path = '/data/web_static/releases/{}'.format(folder_name)
    tmp = "/tmp/" + filename
    put(archive_path, "/tmp/")
    run('mkdir -p {}'.format(release_path))
    run('tar -xzf {} -C {}'.format(tmp, release_path))
    run('rm  /tmp/{}'.format(filename))
    run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(folder_name, folder_name))
    # Delete the archive from the web server
    run('rm -rf /data/web_static/releases/{}/web_static'.format(folder_name))
    # Delete the symbolic link /data/web_static/current
    run('rm -rf /data/web_static/current')
    # Create a new symbolic link to the new version
    run('ln -s {} /data/web_static/current'.format(release_path))
    print("New version deployed!")
    return True
