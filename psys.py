import sys

try:
    x = 1/ 0
except Exception:
    print(sys.exc_info())

print(sys.path)
print(sys.platform)
print(sys.version)
print(sys.version_info)