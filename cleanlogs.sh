#!/bin/bash

## This shell script empties syslog-ng /var/log files

## By Enigma

if [ -f /var/log/auth.log ]
	then
	echo "" > /var/log/auth.log
		if [ -f /var/log/auth.log.old ]
			then
			rm /var/log/auth.log.old
		fi
fi

if [ -f /var/log/dmesg ]
	then
	echo "" > /var/log/dmesg
		if [ -f /var/log/dmesg.old ]
			then
			rm /var/log/dmesg
		fi
fi

if [ -f /var/log/messages ]
	then
	echo "" > /var/log/messages
		if [ -f /var/log/messages.old ]
			then
			rm /var/log/messages.old
		fi
fi
