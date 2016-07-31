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
print_log = ("\n\033[92m\t/var/log:\033[0m")
print_log_ = ("\n\033[93m\t/var/log/ does not exist\033[0m")
perm_denied = ("\n\033[91m\tPermission denied\033[0m")

# Init system

def _init():
    rc_filename = '/etc/rc.conf'
    sysd_filename = '/etc/systemd'
    runit_filename = '/var/service'
    if os.path.isfile(rc_filename):
        print (print_openrc)
        os.system('rc-status')
    elif os.path.isfile(sysd_filename):
        print (print_sysd)
        os.system('systemctl-status')
    elif os.path.isfile(runit_filename):
        print (print_runit)
        if os.access(runit_filename, os.R_OK):
            with open(runit_filename, 'r') as file:
                print (file.read())
            file.close()
        else:
            print (perm_denied)
    else:
        print (print_init_)

# Mount

def _mounts():
    filename = '/proc/mounts'
    if os.path.isfile(filename):
        print (print_mounts)
        if os.access(filename, os.R_OK):
            with open(filename, 'r') as file:
                print (file.read())
            file.close()
        else:
            print (perm_denied)
    else:
        print (print_mounts_)

# Host

def _hosts():
    filename = '/etc/hosts.allow'
    if os.path.isfile(filename):
        print (print_hosts)
        if os.access(filename, os.R_OK):
            with open(filename, 'r') as file:
                print (file.read())
            file.close()
        else:
            print (perm_denied)
    else:
        print (print_hosts_)

def _passwd():
    filename = '/etc/passwd'
    if os.path.isfile(filename):
        print (print_passwd)
        if os.access(filename, os.R_OK):
            with open(filename, 'r') as file:
                print (file.read())
            file.close()
        else:
            print (perm_denied)
    else:
        print (print_passwd_)

# Cron jobs

def _crontab():
    filename = '/etc/crontab'
    if os.path.isfile(filename):
        print (print_crontab)
        if os.access(filename, os.R_OK):
            with open(filename, 'r') as file:
                print (file.read())
            file.close()
        else:
            print (perm_denied)
    else:
        print (print_crontab_)

def _cron_allow():
    filename = '/etc/cron.allow'
    if os.path.isfile(filename):
        print (print_cron_allow)
        if os.access(filename, os.R_OK):
            with open(filename, 'r') as file:
                print (file.read())
            file.close()
        else:
            print (perm_denied)
    else:
        print (print_cron_allow_)

def _cron_deny():
    filename = '/etc/cron.deny'
    if os.path.isfile(filename):
        print (print_cron_deny)
        if os.access(filename, os.R_OK):
            with open(filename, 'r') as file:
                print (file.read())
            file.close()
        else:
            print (perm_denied)
    else:
        print (print_cron_deny_)

def _cron_hourly():
    pathname = '/etc/cron.hourly'
    if os.path.isdir(pathname):
        print (print_cron_hourly)
        if os.access(pathname, os.R_OK):
            for file in os.listdir(pathname):
                print (file)
        else:
            print (perm_denied)
    else:
        print (print_cron_hourly_)

def _cron_daily():
    pathname = '/etc/cron.daily'
    if os.path.isdir(pathname):
        print (print_cron_daily)
        if os.access(pathname, os.R_OK):
            for file in os.listdir(pathname):
                print (file)
        else:
            print (perm_denied)
    else:
        print (print_cron_daily_)

def _cron_weekly():
    pathname = '/etc/cron.weekly'
    if os.path.isdir(pathname):
        print (print_cron_weekly)
        if os.access(pathname, os.R_OK):
            for file in os.listdir(pathname):
                print (file)
        else:
            print (perm_denied)
    else:
        print (print_cron_weekly_)

def _cron_monthly():
    pathname = '/etc/cron.monthly'
    if os.path.isdir(pathname):
        print (print_cron_monthly)
        if os.access(pathname, os.R_OK):
            for file in os.listdir(pathname):
                print (file)
        else:
            print (perm_denied)
    else:
        print (print_cron_monthly_)

# Logs

def _log():
    pathname = '/var/log/'
    if os.path.isdir(pathname):
        print (print_log)
        if os.access(pathname, os.R_OK):
            for file in os.listdir(pathname):
                print (file)
        else:
            print (perm_denied)
    else:
        print (print_log_)

## Main function

def main():
    _init()
    _mounts()
    _hosts()
    _passwd()
    _crontab()
    _cron_allow()
    _cron_deny()
    _cron_hourly()
    _cron_daily()
    _cron_weekly()
    _cron_monthly()
    _log()
main()
