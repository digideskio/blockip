#!/usr/bin/env python
# -*- coding: utf-8 -*-

# blockip: easy-to-use command to add or delete an IP-address to the blocklist in iptables

import sys
import getopt
import subprocess

_name    = "blockip"
_version = "0.1"

def main(argv):
	try:
		opts, args = getopt.getopt(argv, "ha:d:lv", ["help", "add=", "delete=", "list", "version"])

		if len(opts) == 0:
			# Adding without -a or --add: iptables 1.2.3.4 2.3.4.5
			if len(args) > 0:
				opts = []
				for arg in args:
					opts.append(("-a", arg))
			# Display help if no args exist
			else:
				opts = [("-h","")]

		for opt, arg in opts:
			if opt in ("-h", "--help"):
				help()
			elif opt in ("-v", "--version"):
				print version()
			elif opt in ("-a", "--add"):
				subprocess.call(["iptables", "-A", "INPUT", "-s", arg, "-j", "DROP"])
			elif opt in ("-d", "--delete"):
				subprocess.call(["iptables", "-D", "INPUT", "-s", arg, "-j", "DROP"])
			elif opt in ("-l", "--list"):
				subprocess.call(["iptables", "-L", "-n"])
	except getopt.GetoptError, err:
		print "Error: " + str(err)
		sys.exit(2)

def version():
	global _name, _version
	return _name + " " + _version

def help():
	print version()
	print "Usage: blockip [ips|-h|-a ip|-d ip|-l]\n"
	print "-h, --help:			Displays this message."
	print "ips:				Adds IP-addresses to the block list. Example:\n\tblockip 1.2.3.4 2.3.4.5"
	print "-a ip, --add ip:		Adds an IP-address to the block list. Example:\n\tblockip -a 1.2.3.4"
	print "-d ip, --delete ip:		Removes an IP-address from the block list. Example:\n\tblockip -d 1.2.3.4"
	print "-l, --list:			Lists the blocked IP-addresses."
	print "-v, --version:			Displays the version of the utility."

if __name__ == "__main__":
	main(sys.argv[1:])
