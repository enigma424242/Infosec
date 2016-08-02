#!/usr/bin/env python
# utf-8

## This Python script prints operating system information
## By Enigma

## Notes:
# * Requires root privilege

## Compatible:
# * GNU/Linux
# * dev-lang/python:2.7 (stable)
# * dev-lang/python:3.4 (stable)

## Support:
# * OpenRC
# * Systemd
# * Runit
# * Crond

import os

## Color Codes:
# Green (Success) = \033[92m
# Orange (Warning) = \033[93m
# Red (Error) = \033[91m

## Global print variables

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

## Global file/path variables

mounts_filename = '/proc/mounts'
hosts_filename = '/etc/hosts.allow'
passwd_filename = '/etc/passwd'
crontab_filename = '/etc/crontab'
rc_filename = '/etc/rc.conf'
sysd_filename = '/etc/systemd'
runit_filename = '/var/service'
cron_allow_filename = '/etc/cron.allow'
cron_deny_filename = '/etc/cron.deny'

cron_hourly_pathname = '/etc/cron.hourly'
cron_daily_pathname = '/etc/cron.daily'
cron_weekly_pathname = '/etc/cron.weekly'
cron_monthly_pathname = '/etc/cron.monthly'
logs = '/var/log'

## Init system status

def initstatus(file1, file2, file3):
    if os.path.isfile(file1):
        print(print_openrc)
        os.system('rc-status')
    elif os.path.isfile(file2):
        print(print_sysd)
        os.system('systemctl-status')
    elif os.path.isfile(file3):
        print(print_runit)
        if os.access(runit_filename, os.R_OK):
            with open(runit_filename, 'r') as file:
                print(file.read())
            file.close()
        else:
            print(perm_denied)
    else:
        print(print_init_)

## Call init system status

initstatus(rc_filename, sysd_filename, runit_filename)

## Read file

def readfile(filename, pfilename, pfilename_):
    if os.path.isfile(filename):
        print (pfilename)
        if os.access(filename, os.R_OK):
            with open(filename, 'r') as file:
                print(file.read())
            file.close()
        else:
            print(perm_denied)
    else:
        print(pfilename_)

## Call read file

readfile(mounts_filename, print_mounts, print_mounts_)
readfile(hosts_filename, print_hosts, print_hosts_)
readfile(passwd_filename, print_passwd, print_passwd_)
readfile(cron_allow_filename, print_cron_allow, print_cron_allow_)
readfile(cron_deny_filename, print_cron_deny, print_cron_deny_)

## List directory

def listdirectory(pathname, pdirectory, pdirectory_):
    if os.path.isdir(pathname):
        print(pdirectory)
        if os.access(pathname, os.R_OK):
            for file in os.listdir(pathname):
                print(file)
        else:
            print(perm_denied)
    else:
        print(pdirectory_)

## Call list directory

listdirectory(cron_hourly_pathname, print_cron_hourly, print_cron_hourly_)
listdirectory(cron_daily_pathname, print_cron_daily, print_cron_daily_)
listdirectory(cron_weekly_pathname, print_cron_weekly, print_cron_weekly_)
listdirectory(cron_monthly_pathname, print_cron_monthly, print_cron_monthly_)
listdirectory(logs, print_logs, print_logs_)
