import platform
import sys
white = '\x1b[1;37m'
rad = '\x1b[38;5;160m'
green = '\x1b[38;5;46m'
print(f'\033[1;32m<\033[1;31m!\033[1;32m> CHECKING FOR UPDATES...!  ')
hexx = platform.architecture()[0]

if hexx == '64bit':
    print(f'\033[1;32m<\033[1;31m!\033[1;32m> YOUR DEVICE IS 64Bit WELCOME  ')
    import supra as SUPRA
elif hexx == '32bit':
    print(f'\033[1;32m<\033[1;31m!\033[1;32m> NOT AVAILABLE FOR 32Bit WAIT FOR THE NEW UPDATES  ')
    
else:
    print("Architecture not supported:", arch)
    sys.exit()

if hasattr(SUPRA, "main"):
    SUPRA.main()
else:
    print("No main() found in module.")
