import os

file = "text.txt"

if os.path.isfile(file):
    print("available")
else:
    print("unavailable")