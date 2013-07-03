#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from fabric.api import run, put


config_path = os.path.realpath('../supervisor/')
config_file = os.path.basename(config_path)
supervisor_etc_path = "/etc/supervisor/conf.d/"


def supervisor_reset():
    "Reset supervisor"
    run("service supervisor restart")


def supervisor_start():
    "Start supervisor"
    run("service supervisor start")


def supervisor_stop():
    "Stop supervisor"
    run("service supervisor stop")


def supervisor_upload_file_config(supervisor_config_path):
    "Send supervisor configuration"
    put(supervisor_config_path, supervisor_etc_path)


def supervisor_config(config_path=config_path):
    "Send all supervisors configurations"
    for file_name in os.listdir(config_path):
        supervisor_upload_file_config(os.path.join(config_path, file_name))


def supervisor_reload():
    "Reload supervisor config files"
    run("supervisorctl reload")
    run("supervisorctl update")


def supervisor_reset_gunicorn():
    "Reset gunicorn"
    run("supervisorctl restart mark42")


def supervisor(*args):
    "Send supervisor command"
    run("supervisorctl " + " ".join(args))


def supervisor_disable_site(supervisor_config_file):
    "Disable supervisor site"
    run("rm " + supervisor_etc_path + supervisor_config_file)
