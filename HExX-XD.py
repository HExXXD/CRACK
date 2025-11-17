import os, platform, time, sys
white = '\x1b[1;37m'
rad = '\x1b[38;5;160m'
green = '\x1b[38;5;46m'
print(f' {rad}[{white}◆{rad}] {green}Checking For Update...')

hexx = platform.architecture()[0]
if hexx == '64bit':
 print(f' {rad}[{white}◆{rad}] {green}Your Device is 64bit')
 import hexx_64
elif hexx == '32bit':
 print(f' {rad}[{white}◆{rad}] {green}Your Devive is 32bit')
 import hexx_32
