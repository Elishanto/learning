from itertools import combinations

with open('input.txt') as f:
    n, k = list(map(int, f.readline().split()))

l = []
l.extend(range(1, n + 1))
unique = [",".join(map(str, comb)) for comb in combinations(l, k)]

print(unique)
