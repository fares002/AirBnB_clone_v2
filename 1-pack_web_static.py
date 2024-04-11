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

def do_pack():
    # Create directory if it doesn't exist
    local('mkdir -p versions')
    
    # Generate unique timestamp for the archive
    time_str = datetime.now().strftime('%Y%m%d%H%M%S')
    archive = 'web_static_{}.tgz'.format(time_str)
    
    # Compress web_static folder into a .tgz archive
    local('tar -czvf versions/{} web_static'.format(archive))
    
    # Calculate archive size
    archive_path = "versions/{}".format(archive)
    archive_size = os.path.getsize(archive_path)
    
    # Print details of the created archive
    print('web_static packed: {} -> {} bytes'.format(archive_path, archive_size))



