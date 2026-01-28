import os
import sys

# 1. التأكد من وجود ملف supra وإعطائه صلاحية التشغيل
def setup():
    if os.path.exists("supra"):
        os.system("chmod +x supra")
    else:
        print("Error: File 'supra' not found!")
        sys.exit()

# 2. وظيفة تشغيل الأداة
def start_tool():
    print("--- Starting Supra Tool ---")
    # محاولة تشغيل الملف الثنائي (الذي قمت بترجمته أو الموجود مسبقاً)
    try:
        os.system("./supra")
    except Exception as e:
        print(f"Failed to execute: {e}")

# 3. نقطة البداية
if __name__ == "__main__":
    setup()
    start_tool()
