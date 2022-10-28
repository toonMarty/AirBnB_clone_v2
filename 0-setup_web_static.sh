#!/usr/bin/env bash
# a Bash script that sets up the web servers for the deployment of web_static
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
