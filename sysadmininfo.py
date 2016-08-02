#!/usr/bin/env python
# utf-8

# This Python script prints operating system information
# By Enigma

## Notes:
#  * Requires root privilege

## Compatible:
#  * GNU/Linux
#  * dev-lang/python:2.7 (stable)
#  * dev-lang/python:3.4 (stable)

## Support:
#  * OpenRC
#  * Systemd
#  * Runit
#  * Crond

import os

## Global print variables
#  Color codes

success = '\n\033[92m\t'
warning = '\n\033[93m\t'
error = '\n\033[91m\t'
escape = '\033[0m'

print_openrc = '%s rc-status: %s' % (success, escape)
print_sysd = '%s systemctl-status: %s' % (success, escape)
print_runit = '%s /var/service: %s' % (success, escape)
print_init_ = '%s no init status available %s' % (warning, escape)

print_mounts = '%s /proc/mounts: %s' % (success, escape)
print_mounts_ = '%s /proc/mounts does not exist %s' % (warning, escape)
print_hosts = '%s Trusted host relationship: %s' % (success, escape)
print_hosts_ = '%s /etc/hosts.allow does not exist %s' % (warning, escape)
print_passwd = '%s Account creation: %s' % (success, escape)
print_passwd_ = '%s /etc/passwd does not exist %s' % (warning, escape)
print_crontab = '%s /etc/crontab: %s' % (success, escape)
print_crontab_ = '%s /etc/crontab does not exist %s' % (warning, escape)
print_cron_allow = '%s /etc/cron.allow: %s' % (success, escape)
print_cron_allow_ = '%s /etc/cron.allow does not exist %s' % (warning, escape)
print_cron_deny = '%s /etc/cron.deny: %s' % (success, escape)
print_cron_deny_ = '%s /etc/cron.deny does not exist %s' % (warning, escape)

print_cron_hourly = '%s /etc/cron.hourly/: %s' % (success, escape)
print_cron_hourly_ = '%s /etc/cron.hourly/ does not exist %s' % (warning, escape)
print_cron_daily = '%s /etc/cron.daily/: %s' % (success, escape)
print_cron_daily_ = '%s /etc/cron.daily/ does not exist %s' % (warning, escape)
print_cron_weekly = '%s /etc/cron.weekly/: %s' % (success, escape)
print_cron_weekly_ = '%s /etc/cron.weekly/ does not exist %s' % (warning, escape)
print_cron_monthly = '%s /etc/cron.monthly/: %s' % (success, escape)
print_cron_monthly_ = '%s /etc/cron.monthly/ does not exist %s' % (warning, escape)
print_logs = '%s /var/log: %s' % (success, escape)
print_logs_ = '%s /var/log/ does not exist %s' % (warning, escape)
perm_denied = '%s Permission denied %s' % (error, escape)

## Class containers

class init(object):

    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

# Init status function

    def initstatus(self):
        if os.path.isfile(self.arg1):
            print(print_openrc)
            os.system('rc-status')
        elif os.path.isfile(self.arg2):
            print(print_sysd)
            os.system('systemctl-status')
        elif os.path.isfile(self.arg3):
            print(print_runit)
            if os.access(self.arg3, os.R_OK):
                with open(self.arg3, 'r') as file:
                    print(file.read())
                file.close()
            else:
                print(perm_denied)
        else:
            print(print_init_)

class readfile(object):

    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

# Read file function

    def readfunction(self):
        if os.path.isfile(self.arg1):
            print(self.arg2)
            if os.access(self.arg1, os.R_OK):
                with open(self.arg1, 'r') as file:
                    print(file.read())
                file.close()
            else:
                print(perm_denied)
        else:
            print(self.arg3)

class listdirectory(object):

    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

# List directory function

    def listfunction(self):
        if os.path.isdir(self.arg1):
            print(self.arg2)
            if os.access(self.arg1, os.R_OK):
                for file in os.listdir(self.arg1):
                    print(file)
            else:
                print(perm_denied)
        else:
            print(self.arg3)

## Assigning class arguments

sysinit = init('/etc/rc.conf', '/etc/systemd', '/var/service')

mounts = readfile('/proc/mounts', print_mounts, print_mounts_)
hosts = readfile('/etc/hosts.allow', print_hosts, print_hosts_)
passwd = readfile('/etc/passwd', print_passwd, print_passwd_)
crontab = readfile('/etc/crontab', print_crontab, print_crontab_)
cronallow = readfile('/etc/cron.allow', print_cron_allow, print_cron_allow_)
crondeny = readfile('/etc/cron.deny', print_cron_deny, print_cron_deny_)

cronhourly = listdirectory('/etc/cron.hourly', print_cron_hourly, print_cron_hourly_)
crondaily = listdirectory('/etc/cron.daily', print_cron_daily, print_cron_daily_)
cronweekly = listdirectory('/etc/cron.weekly', print_cron_weekly, print_cron_weekly_)
cronmonthly = listdirectory('/etc/cron.monthly', print_cron_monthly, print_cron_monthly_)
logs = listdirectory('/var/log', print_logs, print_logs_)

## Calling class functions

sysinit.initstatus()

mounts.readfunction()
hosts.readfunction()
passwd.readfunction()
crontab.readfunction()
cronallow.readfunction()
crondeny.readfunction()

cronhourly.listfunction()
crondaily.listfunction()
cronweekly.listfunction()
cronmonthly.listfunction()
logs.listfunction()
