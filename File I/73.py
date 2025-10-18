import os

file = "text.txt"

with open(file, "r") as file:
    file_row = sum(1 for line in file)
    print(file_row)

