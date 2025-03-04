import os
import string

with open(r"C:\\ALL LABKA\\labs\\lab 6\\dif-and-files\\sometext.txt", "r", encoding="utf-8") as f:
   data = f.read()  

print(len(list(data.split("\n"))))
f.close()