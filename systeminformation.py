#!/usr/bin/env python
# coding: utf-8

# Title: System Information v1.02
# Author: Enigma

import os

class InitSystemStatus(object):

    def init_status(self, filename, command):
        if os.path.exists(filename):
            print("\ninit system status:\n")
            os.system(command)

class FilePath(object):

    def file_path(self, pathname):
        if os.path.isfile(pathname):
            print("\n")
            print(pathname)
            if os.access(pathname, os.R_OK):
                with open(pathname, 'r') as file:
                    print(file.read())
                file.close()
            else:
                print("Permission Denied")
        elif os.path.isdir(pathname):
            print("\n")
            print(pathname)
            if os.access(pathname, os.R_OK):
                for file in os.listdir(pathname):
                    print(file)
            else:
                print("Permission Denied")
        else:
            print(filename, "Does not exist")

init = InitSystemStatus()
path = FilePath()

initsystemstatus = {
    'openrc': init.init_status('/bin/rc-status', 'rc-status'),
    'systemd': init.init_status('/bin/systemctl-status', 'systemctl-status')
    }

filepath = {
    'mounts': path.file_path('/proc/mounts'),
    'hosts': path.file_path('/etc/hosts.allow'),
    'passwd': path.file_path('/etc/passwd'),
    'crontab': path.file_path('/etc/crontab'),
    'cronallow': path.file_path('/etc/cron.allow'),
    'crondeny': path.file_path('/etc/cron.deny'),
    'cronhourly': path.file_path('/etc/cron.hourly'),
    'crondaily': path.file_path('/etc/cron.daily'),
    'cronweekly': path.file_path('/etc/cron.weekly'),
    'cronmonthly': path.file_path('/etc/cron.monthly'),
    'logs': path.file_path('/var/log')
    }

