#!/usr/bin/env python
# coding: utf-8

# Title: System Information v1.01
# Author: Enigma

import os

class InitStatus(object):

    def initstatus(self, filename, command):
        if os.path.exists(filename):
            print("\n-------")
            print("Init System Status:")
            print("-------\n")
            os.system(command)

class FilePath(object):

    def filepath(self, pathname):
        if os.path.exists(pathname):
            print("\n-------")
            print(pathname)
            print("-------\n")
            if os.access(pathname, os.R_OK):
                if os.path.isfile(pathname):
                    with open(pathname, "r") as file:
                        print(file.read())
                    file.close()
                else:
                    os.path.isdir(pathname)
                    for file in os.listdir(pathname):
                        print(file)
            else:
                print("Permission Denied")
        else:
            print(pathname, "Does not exist")

class Phase(object):

    """For future updates I set the instance calls to key value pairs."""

    system_init = InitStatus()
    system_path = FilePath()

    init_status = {
        "openrc": system_init.initstatus("/bin/rc-status", "rc-status"),
        "systemd": system_init.initstatus("/bin/systemctl-status", "systemctl-status")
    }

    file__path = {
        "mounts": system_path.filepath("/proc/mounts"),
        "hosts": system_path.filepath("/etc/hosts.allow"),
        "passwd": system_path.filepath("/etc/passwd"),
        "crontab": system_path.filepath("/etc/crontab"),
        "cronallow": system_path.filepath("/etc/cron.allow"),
        "crondeny": system_path.filepath("/etc/cron.deny"),
        "cronhourly": system_path.filepath("/etc/cron.hourly"),
        "crondaily": system_path.filepath("/etc/cron.daily"),
        "cronweekly": system_path.filepath("/etc/cron.weekly"),
        "cronmonthly": system_path.filepath("/etc/cron.monthly"),
        "logs": system_path.filepath("/var/log")
    }
