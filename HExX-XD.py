import os, platform, time, sys

print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mChecking For Update...')

hexx = platform.architecture()[0]
if hexx == '64bit':
 print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mYour Device is 64bit')
 import hexx_64
elif hexx == '32bit':
 print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mYour Devive is 32bit')
 import hexx_32
