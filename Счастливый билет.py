def root(number):
    while number >= 10:
        number = sum(map(int,str(number)))
    return number


ticket = input().strip()

found = False
for i in range(1, len(ticket)):
    if root(int(ticket[0:i])) == root(int(ticket[i:len(ticket)])):
        found = True
        break

if found:
    print(1)
    print(ticket[0:round(len(ticket) / 2)])
else:
    print(0)