import platform
import os

print("platform:", platform.system())
print("build_for", os.getenv('BUILDFOR'))