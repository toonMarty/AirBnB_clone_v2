#!/usr/bin/python3

"""This module contains a Fabric script that generates a .tgz
    archive from the contents of the
    web_static folder of the  AirBnB Clone repo
"""
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """This function creates a .tgz archive of web_static"""
    cur_dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        cur_dt.year,
        cur_dt.month,
        cur_dt.day,
        cur_dt.hour,
        cur_dt.minute,
        cur_dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None

    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
