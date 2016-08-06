#!/bin/bash

## This shell script searches for error and warnings within syslog-ng /var/log/

## By Enigma

if [ -f /var/log/auth.log ]
	then
	grep 'error' -i /var/log/auth.log
	grep 'warning' -i /var/log/auth.log
		if [ -f /var/log/auth.log.old ]
			then
			grep 'error' -i /var/log/auth.log.old
			grep 'warning' -i /var/log/auth.log.old
		fi
fi

if [ -f /var/log/dmesg ]
	then
	grep 'error' -i /var/log/dmesg
	grep 'warning' -i /var/log/dmesg
		if [ -f /var/log/dmesg.old ]
			then
			grep 'error' -i /var/log/dmesg.old
			grep 'warning' -i /var/log/dmesg.old
		fi
fi

if [ -f /var/log/messages ]
	then
	grep 'error' -i /var/log/messages
	grep 'warning' -i /var/log/messages
		if [ -f /var/log/messages.old ]
			then
			grep 'error' -i /var/log/messages.old
			grep 'warning' -i /var/log/messages.old
		fi
fi

if [ -f /var/log/Xorg.0.log ]
	then
	grep 'error' -i /var/log/Xorg.0.log
	grep 'warning' -i /var/log/Xorg.0.log
		if [ -f /var/log/Xorg.0.log.old ]
			then
			grep 'error' -i /var/log/Xorg.0.log.old
			grep 'warning' -i /var/log/Xorg.0.log.old
		fi
fi
