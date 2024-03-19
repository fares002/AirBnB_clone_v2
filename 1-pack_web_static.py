#!/usr/bin/python3
# generates an archieve.
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """make an archeiev"""
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
