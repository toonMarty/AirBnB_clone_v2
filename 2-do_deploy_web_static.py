#!/usr/bin/python3
"""This module contains a Fabric script
   (based on the file 1-pack_web_static.py) that distributes an
      archive to your web servers, using the function do_deploy
      """

import os
from fabric.api import run, put, env

env.hosts = ['3.238.234.192', '52.91.151.139']
env.user = "ubuntu"


def do_deploy(archive_path):
    """This function creates a tar of web-static"""
    if os.path.exists(archive_path) is False:
        return False
    else:
        try:
            put(archive_path, "/tmp/")
            file_name = archive_path.split("/")[1]
            file_name2 = file_name.split(".")[0]
            final_name = "/data/web_static/releases/" + file_name2 + "/"
            run("mkdir -p " + final_name)
            run("tar -xzf /tmp/" + file_name + " -C " + final_name)
            run("rm /tmp/" + file_name)
            run("mv " + final_name + "web_static/* " + final_name)
            run("rm -rf " + final_name + "web_static")
            run("rm -rf /data/web_static/current")
            run("ln -s " + final_name + " /data/web_static/current")
            print("New version deployed!")
            return True
        except Exception:
            return False
