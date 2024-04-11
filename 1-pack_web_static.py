#!/usr/bin/env python3
"""
 Fabric script that generates 
 a .tgz archive from the contents of 
 the web_static folder of your 
 AirBnB Clone repo, using the function do_pack    
"""
from fabric.api import *
from datetime import datetime
import os

time = datetime.now()
time_str = time.strftime('%Y%m%d%H%M%S')
archive = 'web_static_' + time_str + '.tgz'

def do_pack():
    local('sudo mkdir -p versions')
    local(f'tar -cvzf versions/{archive}')
    archive_path = f"versions/{archive}"
    archive_size = os.path.getsize(archive_path)
    print (f'web_static packed: {archive_path} -> {archive_size}')
