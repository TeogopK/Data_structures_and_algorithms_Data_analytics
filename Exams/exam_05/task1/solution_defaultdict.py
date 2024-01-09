from collections import defaultdict

N = int(input())
ids = [int(input()) for _ in range(N)]

d = defaultdict(int)

for id in ids:
    d[id] += 1
    d[id] %= 10

users = 0
for id in set(ids):
    if d[id] != 0:
        users += 1

# users = sum(0 if d[id] == 0 else 1 for id in set(ids))
products = sum(d[id] for id in set(ids))

print(users, products)