import re


password = input().strip()

L = 0

last = 1
for char in list(password):
    if re.match('[а-я]', char):
        if last != 0:
            L += 1
        last = 0
    elif re.match('[a-z]', char):
        if last != 1:
            L += 1
        last = 1
print((L + 1) * len(password))