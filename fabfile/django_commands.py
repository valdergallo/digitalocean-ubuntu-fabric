#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __init__ import py, virtualenv


def migrate():
    "Django Syncdb"
    with virtualenv():
        py('manage.py migrate')


def shell():
    "Django Shell"
    with virtualenv():
        py('manage.py shell')


def dbshell():
    "Django DB Shell"
    with virtualenv():
        py('manage.py dbshell')


def syncdb():
    "South Migration"
    with virtualenv():
        py('manage.py syncdb')


def static():
    "Collect Static Files"
    with virtualenv():
        py('manage.py collectstatic -l --noinput')


def command(*args):
    "Send custom command with args or not. Usage: fab command:mycustom,123 or fab command:mycustom"
    with virtualenv():
        py('manage.py ' + " ".join(args))
