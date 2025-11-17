import platform
import sys
white = '\x1b[1;37m'
rad = '\x1b[38;5;160m'
green = '\x1b[38;5;46m'
print(f' {rad}[{white}◆{rad}] {green}Checking For Update...')
arch = platform.machine()

if arch in ["aarch64", "arm64", "armv8l"]:
    print(f' {rad}[{white}◆{rad}] {green}Your Device is 64bit')
    import hexx_64 as HExX
elif arch in ["armv7l", "arm", "armeabi", "armeabi-v7a"]:
    print(f' {rad}[{white}◆{rad}] {green}Your Device is 32bit')
    import hexx_32 as HExX
else:
    print("Architecture not supported:", arch)
    sys.exit()

if hasattr(HExX, "main"):
    HExX.main()
else:
    print("No main() found in module.")
