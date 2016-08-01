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

# Color Codes:
# Green (Success) = \033[92m
# Orange (Warning) = \033[93m
# Red (Error) = \033[91m

## Global Print Variables

print_openrc = ("\n\033[92m\trc-status:\033[0m")
print_sysd = ("\n\033[92m\tsystemctl-status:\033[0m")
print_runit = ("\n\033[92m\t/var/service:\033[0m")
print_init_ = ("\n\033[93m\tno init status available\033[0m")
print_mounts = ("\n\033[92m\t/proc/mounts:\033[0m")
print_mounts_ = ("\n\033[93m\t/proc/mounts does not exist\033[0m")
print_hosts = ("\n\033[92m\tTrusted host relationship:\033[0m")
print_hosts_ = ("\n\033[93m\t/etc/hosts.allow does not exist\033[0m")
print_passwd = ("\n\033[92m\tAccount creation:\033[0m")
print_passwd_ = ("\n\033[93m\t/etc/passwd does not exist\033[0m")
print_crontab = ("\n\033[92m\t/etc/crontab:\033[0m")
print_crontab_ = ("\n\033[93m\t/etc/crontab does not exist\033[0m")
print_cron_allow = ("\n\033[92m\t/etc/cron.allow:\033[0m")
print_cron_allow_ = ("\n\033[93m\t/etc/cron.allow does not exist\033[0m")
print_cron_deny = ("\n\033[92m\t/etc/cron.deny:\033[0m")
print_cron_deny_ = ("\n\033[93m\t/etc/cron.deny does not exist\033[0m")
print_cron_hourly = ("\n\033[92m\t/etc/cron.hourly/:\033[0m")
print_cron_hourly_ = ("\n\033[93m\t/etc/cron.hourly/ does not exist\033[0m")
print_cron_daily = ("\n\033[92m\t/etc/cron.daily/:\033[0m")
print_cron_daily_ = ("\n\033[93m\t/etc/cron.daily/ does not exist\033[0m")
print_cron_weekly = ("\n\033[92m\t/etc/cron.weekly/:\033[0m")
print_cron_weekly_ = ("\n\033[93m\t/etc/cron.weekly/ does not exist\033[0m")
print_cron_monthly = ("\n\033[92m\t/etc/cron.monthly/:\033[0m")
print_cron_monthly_ = ("\n\033[93m\t/etc/cron.monthly/ does not exist\033[0m")
print_logs = ("\n\033[92m\t/var/log:\033[0m")
print_logs_ = ("\n\033[93m\t/var/log/ does not exist\033[0m")
perm_denied = ("\n\033[91m\tPermission denied\033[0m")

# Global File/Path Variables

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
logs = '/var/logs'

## Init System Status Function

def initstatus(file1, file2, file3):
    if os.path.isfile(file1):
        print (print_openrc)
        os.system('rc-status')
    elif os.path.isfile(file2):
        print (print_sysd)
        os.system('systemctl-status')
    elif os.path.isfile(file3):
        print (print_runit)
        if os.access(runit_filename, os.R_OK):
            with open(runit_filename, 'r') as file:
                print (file.read())
            file.close()
        else:
            print (perm_denied)
    else:
        print (print_init_)

## Call Init System Status Function

initstatus(rc_filename, sysd_filename, runit_filename)

## Read File Function

def readfile(filename, pfilename, pfilename_):
    if os.path.isfile(filename):
        print (pfilename)
        if os.access(filename, os.R_OK):
            with open(filename, 'r') as file:
                print (file.read())
            file.close()
        else:
            print (perm_denied)
    else:
        print (pfilename_)

## Call Read File Function

readfile(mounts_filename, print_mounts, print_mounts_)
readfile(hosts_filename, print_hosts, print_hosts_)
readfile(passwd_filename, print_passwd, print_passwd_)
readfile(cron_allow_filename, print_cron_allow, print_cron_allow_)
readfile(cron_deny_filename, print_cron_deny, print_cron_deny_)

## List Directory Function

def listdirectory(pathname, pdirectory, pdirectory_):
    if os.path.isdir(pathname):
        print (pdirectory)
        if os.access(pathname, os.R_OK):
            for file in os.listdir(pathname):
                print (file)
        else:
            print (perm_denied)
    else:
        print (pdirectory_)

## Call List Directory Function

listdirectory(cron_hourly_pathname, print_cron_hourly, print_cron_hourly_)
listdirectory(cron_daily_pathname, print_cron_daily, print_cron_daily_)
listdirectory(cron_weekly_pathname, print_cron_weekly, print_cron_weekly_)
listdirectory(cron_monthly_pathname, print_cron_monthly, print_cron_monthly_)
listdirectory(logs, print_logs, print_logs_)
