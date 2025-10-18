import os

file = "text.txt"

with open(file, "r") as file:
    read=file.read()
    print(len(read))