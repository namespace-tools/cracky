#!/usr/bin/env python3
#
# Cracky-Py: Because sometimes nothing else works.
#
# USAGE: cracky.py [HashType] [HashFile] [WordList]

from hashlib import *
from sys import argv

HashType = argv[1]

print(
"""\x1b[36m————————————————————————————————————————————————————————————————
\x1b[31m_________                       __            __________
\_   ___ \____________    ____ |  | _____.__. \______   \___.__.
/    \  \/\_  __ \__  \ _/ ___\|  |/ <   |  |  |     ___<   |  |
\     \____|  | \// __ \\  \___|     < \___  |  |    |    \___  |
 \______  /|__|  (____  /\___  >__|_ \/ ____|  |____|    / ____|
        \/            \/     \/     \/\/                 \/
\x1b[36m————————————————————————————————————————————————————————————————\033[0m""")

with open(argv[2]) as infile:
	hash = str.strip(infile.readline())

with open(argv[3], encoding='latin-1') as wordlist:
	for Line in wordlist:
		if globals()[HashType](bytes(Line.strip(), 'latin-1')).hexdigest() == hash:
				print(f">> Password: {Line}\n")
				exit()

print(f" Unable to crack: {hash}")
