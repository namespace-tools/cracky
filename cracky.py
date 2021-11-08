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

with open(argv[2], encoding='latin-1') as infile:
	hash = str.strip(infile.readline())

with open(argv[3]) as wordlist:
	for Line in wordlist:
		x = str.strip(Line)
		if globals()[HashType](bytes(''.join(x),'latin-1')).hexdigest() == hash:
				print(f">> Password: {''.join(x)}\n")
				exit()

print(f" Unable to crack: {hash}")
