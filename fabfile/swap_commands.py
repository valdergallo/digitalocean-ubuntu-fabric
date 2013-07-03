#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from fabric.api import run, cd, put
from fabric.colors import green


def free():
    "Show free memory"
    run("free -m")


def df():
    "Partition info"
    run("df -h")


def swap():
    "List swap"
    run("swapon -s")


def swapon():
    "Add a Swap File"
    run("fallocate -l 512M /swapfile")
    run("ls -lh /swapfile")
    run("chmod 600 /swapfile")
    run("mkswap /swapfile")
    run("swapon /swapfile")
    run("free -m")
    run("echo '# Paste this information at the bottom of the file' >> /etc/fstab")
    run("echo '/swapfile    none    swap    defaults    0   0' >> /etc/fstab")
    run("cat /proc/sys/vm/swappiness")
    run("cat /proc/sys/vm/vfs_cache_pressure")
    run("sysctl vm.vfs_cache_pressure=50")
    run("echo '# Search for the vm.swappiness setting.  Uncomment and change it as necessary.' >> /etc/sysctl.conf")
    run("echo 'vm.vfs_cache_pressure = 50' >> /etc/sysctl.conf")
    print(green("Swap ON"))

