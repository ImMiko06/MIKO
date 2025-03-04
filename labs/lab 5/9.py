import re

with open(r"C:\ALL LABKA\labs\lab 5\8-9-10.txt", encoding="utf-8" ) as f:
    data=f.read()

print(re.findall(r"[A-Z][a-z]*", data))


#находит только слова начинающиеся с заглавной буквы и содержащие только строчные буквы символы итд не берет