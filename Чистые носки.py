with open('input.txt') as f:
    n, d = list(map(int, f.readline().split()))
    socks = sorted(list(map(int, f.readline().split())))

days = 0
i = 1
while i < len(socks):
    if abs(socks[i - 1] - socks[i]) <= d:
        days += 1
        i += 2
    else:
        i += 1
print(days)
