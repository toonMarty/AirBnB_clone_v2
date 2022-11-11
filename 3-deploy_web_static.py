#!/usr/bin/python3
"""
Fabric script based on file 2-do_deploy
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir

env.hosts = ['3.238.234.192', '52.91.151.139']


def do_pack():
    """This function generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception:
        return None


def do_deploy(archive_path):
    """This function"""
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_extn = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp')
        run("mkdir -p {}{}/".format(path, no_extn))
        run("tar -xzf /tmp/{} -C {}{}/".format(file_name, path, no_extn))
        run("rm /tmp/{}".format(file_name))
        run("mv {0}{1} / web_static / * {0}{1} /".format(path, no_extn))
        run("rm -rf {}{}/web_static".format(path, no_extn))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, no_extn))
        return True
        except BaseException:
            return False


def deploy():
    """This function creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
