import os

file = "text.txt"
files= "texts.txt"

with open(file, "r") as file:
    read= file.read()
print(read)

with open(files, "w") as file:
    file.write(read)