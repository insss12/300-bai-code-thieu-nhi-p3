import os

file = "text.txt"

with open(file, "r") as file:
    text = file.read()

print(text)


