#!/usr/bin/env python
# utf-8

## System Information
## By Enigma

## Notes:
# * Requires root privilege

## PEP8 Compliant

## Compatible:
# * GNU/Linux

## Support:
# * OpenRC
# * Systemd
# * Runit
# * Crond

import os

class InitSystemStatus(object):

    def initsystem(self, filename, command):
        if os.path.exists(filename):
            print('\n')
            print('init system status:')
            print('\n')
            os.system(command)

class FilePath(object):

    def readfile(self, filename):
        if os.path.isfile(filename):
            print('\n')
            print(filename)
            print('\n')
            if os.access(filename, os.R_OK):
                with open(filename, 'r') as file:
                    print(file.read())
                file.close()
            else:
                print("Permission Denied")
        else:
            print(filename, "Does not exist")

    def listdirectory(self, pathname):
        if os.path.isdir(pathname):
            print('\n')
            print(pathname)
            print('\n')
            if os.access(pathname, os.R_OK):
                for file in os.listdir(pathname):
                    print(file)
            else:
                print("Permission Denied")
        else:
            print(pathname, "Does not exist")

init = InitSystemStatus()
filepath = FilePath()

structure = {
    'openrc': init.initsystem('/bin/rc-status', 'rc-status'),
    'systemd': init.initsystem('/bin/systemctl-status', 'systemctl-status'),
    'mounts': filepath.readfile('/proc/mounts'),
    'hosts': filepath.readfile('/etc/hosts.allow'),
    'passwd': filepath.readfile('/etc/passwd'),
    'crontab': filepath.readfile('/etc/crontab'),
    'cronallow': filepath.readfile('/etc/cron.allow'),
    'crondeny': filepath.readfile('/etc/cron.deny'),
    'cronhourly': filepath.listdirectory('/etc/cron.hourly'),
    'crondaily': filepath.listdirectory('/etc/cron.daily'),
    'cronweekly': filepath.listdirectory('/etc/cron.weekly'),
    'cronmonthly': filepath.listdirectory('/etc/cron.monthly'),
    'logs': filepath.listdirectory('/var/log')
    }
