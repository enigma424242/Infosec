#!/usr/bin/env python
# coding: utf-8

# Title: System Information v1.01
# Author: Enigma

import os

class InitSystemStatus(object):

    def init_status(self, filename, command):
        if os.path.exists(filename):
            print("\ninit system status:\n")
            os.system(command)

class FilePath(object):

    def read_file(self, filename):
        if os.path.isfile(filename):
            print("\n")
            print(filename)
            if os.access(filename, os.R_OK):
                with open(filename, 'r') as file:
                    print(file.read())
                file.close()
            else:
                print("Permission Denied")
        else:
            print(filename, "Does not exist")

    def list_directory(self, pathname):
        if os.path.isdir(pathname):
            print("\n")
            print(pathname)
            if os.access(pathname, os.R_OK):
                for file in os.listdir(pathname):
                    print(file)
            else:
                print("Permission Denied")
        else:
            print(pathname, "Does not exist")

initsystem = InitSystemStatus()
filepath = FilePath()

init = {
    'openrc': initsystem.init_status('/bin/rc-status', 'rc-status'),
    'systemd': initsystem.init_status('/bin/systemctl-status', 'systemctl-status')
    }

files = {
    'mounts': filepath.read_file('/proc/mounts'),
    'hosts': filepath.read_file('/etc/hosts.allow'),
    'passwd': filepath.read_file('/etc/passwd'),
    'crontab': filepath.read_file('/etc/crontab'),
    'cronallow': filepath.read_file('/etc/cron.allow'),
    'crondeny': filepath.read_file('/etc/cron.deny')
    }

directories = {
    'cronhourly': filepath.list_directory('/etc/cron.hourly'),
    'crondaily': filepath.list_directory('/etc/cron.daily'),
    'cronweekly': filepath.list_directory('/etc/cron.weekly'),
    'cronmonthly': filepath.list_directory('/etc/cron.monthly'),
    'logs': filepath.list_directory('/var/log')
    }
