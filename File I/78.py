import os

file = "text.txt"

with open(file, "r") as file:
    for line in file:
        print(line)