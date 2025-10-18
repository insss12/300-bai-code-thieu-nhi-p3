import os

file = "text.txt"
count=0
with open(file, "r") as file:
    for words in file:
        count+=1

print(count)
