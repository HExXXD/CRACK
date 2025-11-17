import platform
import sys

arch = platform.machine()

if arch in ["aarch64", "arm64", "armv8l"]:
    import hexx_64 as HExX
elif arch in ["armv7l", "arm", "armeabi", "armeabi-v7a"]:
    import hexx_32 as HExX
else:
    print("Architecture not supported:", arch)
    sys.exit()

if hasattr(HExX, "main"):
    HExX.main()
else:
    print("No main() found in module.")
