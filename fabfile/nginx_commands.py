#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from fabric.api import run, cd, put
from fabric.colors import green, red


nginx_config_path = os.path.realpath('deploy/nginx/')
nginx_avaliable_path = "/etc/nginx/sites-available/"
nginx_enable_path = "/etc/nginx/sites-enabled/"


def nginx_reset():
    "Reset nginx"
    run("service nginx restart")


def nginx_start():
    "Start nginx"
    run("service nginx start")


def nginx_stop():
    "Stop nginx"
    run("service nginx stop")


def nginx(command):
    "Run service command to nginx"
    run("service nginx " + command)


def nginx_config(nginx_config_path=nginx_config_path):
    "Send nginx configuration"
    for file_name in os.listdir(nginx_config_path):
        put(os.path.join(nginx_config_path, file_name), nginx_avaliable_path)


def nginx_enable_site(nginx_config_file):
    "Enable nginx site"
    with cd(nginx_enable_path):
        run('ln -s ' + nginx_avaliable_path + nginx_config_file)


def nginx_enable_all_site():
    "Enable all sites"
    for file_name in os.listdir(nginx_config_path):
        nginx_enable_site(file_name)


def nginx_disable_site(nginx_config_file):
    "Disable nginx site"
    run("rm " + nginx_enable_path + nginx_config_file)
