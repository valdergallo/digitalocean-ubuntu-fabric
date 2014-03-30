#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fabric.api import run, cd

APT_GET_PACKAGES = [
    "build-essential",
    "git",
    "vim",
    "python-dev",
    "python-virtualenv",
    "python-pip",
]


def setup():
    "Install default packages for django"
    run("apt-get install " + " ".join(APT_GET_PACKAGES))


def setup_webserver():
    "Install default packages for django and NGINX"
    APT_GET_PACKAGES.append("nginx")
    setup()


def create_www():
    "Configure permissions on www"
    run("mkdir -p /www/")
    run("chown -R root:www-data /www/")
    run("chmod 775 -R /www/")
    run("chmod g+s -R /www/")


def create_package(name):
    "Create virtualenv"
    create_www()
    package_name = "/www/%s-package" % str(name)
    run("virtualenv " + package_name)
    with cd(package_name):
        run("mkdir -p logs")
