#!/usr/bin/env python3
#
# Cracky-Py: Because sometimes nothing else works.
#
# USAGE: cracky.py [HashType] [HashFile] [WordList]

from sys import argv
from hashlib import *
from crypt import crypt
from hmac import compare_digest

print(
"""\x1b[36m————————————————————————————————————————————————————————————————
\x1b[31m_________                       __            __________
\_   ___ \____________    ____ |  | _____.__. \______   \___.__.
/    \  \/\_  __ \__  \ _/ ___\|  |/ <   |  |  |     ___<   |  |
\     \____|  | \// __ \\  \___|     < \___  |  |    |    \___  |
 \______  /|__|  (____  /\___  >__|_ \/ ____|  |____|    / ____|
        \/            \/     \/     \/\/                 \/
\x1b[36m————————————————————————————————————————————————————————————————\033[0m""")

# Print the help/system info
if argv[1] == '-l' or argv[1] == '-h':
	print("\tUSAGE: cracky.py [HashType] [HashFile] [WordList]\n")
	print("Available on this system:")
	print("> unix")
	for i in range(0, len(algorithms_available)):
		print("> "+list(algorithms_available)[i])
	exit()

# Load the hash, only one for now
with open(argv[2]) as infile:
	hash = str.strip(infile.readline())

def crack():
# Cracking basic hashes from the hashlib module
	if argv[1].lower() in algorithms_available:
		with open(argv[3], encoding='latin-1') as wordlist:
			for Line in wordlist:
				if globals()[argv[1].lower()](bytes(Line.strip(), 'latin-1')).hexdigest() == hash:
					print(f">> Password: {Line}\n")
					exit()
# Cracking standard UNIX $6 passwords
	elif argv[1].lower() in "unix":
		with open(argv[3], encoding='latin-1') as wordlist:
			for Line in wordlist:
				if compare_digest(crypt(Line.strip(), hash), hash):
					print(f">> Password: {Line}\n")
					exit()
# Fail notice
	print(f" Unable to crack: {hash}")

crack()
