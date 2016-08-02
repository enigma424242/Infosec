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

## Class container

class sysadmin(object):

    def __init__(self, file1, file2, file3):
        self.file1 = file1
        self.file2 = file2
        self.file3 = file3

    def initstatus(self):
        if os.path.isfile(self.file1):
            print (print_openrc)
            os.system('rc-status')
        elif os.path.isfile(self.file2):
            print (print_sysd)
            os.system('systemctl-status')
        elif os.path.isfile(self.file3):
            print (print_runit)
            if os.access(self.file3, os.R_OK):
                with open(self.file3, 'r') as file:
                    print (file.read())
                file.close()
            else:
                print (perm_denied)
        else:
            print (print_init_)

    def readfunction(self):
        if os.path.isfile(self.file1):
            print (self.file2)
            if os.access(self.file1, os.R_OK):
                with open(self.file1, 'r') as file:
            	    print (file.read())
            	file.close()
            else:
            	print (perm_denied)
    	else:
            print (self.file3)

    def listfunction(self):
        if os.path.isdir(self.file1):
            print (self.file2)
            if os.access(self.file1, os.R_OK):
                for file in os.listdir(self.file1):
                    print (file)
            else:
                print (perm_denied)
        else:
            print (self.file3)

## Call functions

init = sysadmin('/etc/rc.conf', '/etc/systemd', '/var/service')
init.initstatus()

readfile = sysadmin('/proc/mounts', print_mounts, print_mounts_)
readfile.readfunction()
readfile = sysadmin('/etc/hosts.allow', print_hosts, print_hosts_)
readfile.readfunction()
readfile = sysadmin('/etc/passwd', print_passwd, print_passwd_)
readfile.readfunction()
readfile = sysadmin('/etc/crontab', print_crontab, print_crontab_)
readfile.readfunction()
readfile = sysadmin('/etc/cron.allow', print_cron_allow, print_cron_allow_)
readfile.readfunction()
readfile = sysadmin('/etc/cron.deny', print_cron_deny, print_cron_deny_)
readfile.readfunction()

listpath = sysadmin('/etc/cron.hourly', print_cron_hourly, print_cron_hourly_)
listpath.listfunction()
listpath = sysadmin('/etc/cron.daily', print_cron_daily, print_cron_daily_)
listpath.listfunction()
listpath = sysadmin('/etc/cron.weekly', print_cron_weekly, print_cron_weekly_)
listpath.listfunction()
listpath = sysadmin('/etc/cron.monthly', print_cron_monthly, print_cron_monthly_)
listpath.listfunction()
listpath = sysadmin('/var/log', print_logs, print_logs_)
listpath.listfunction()
