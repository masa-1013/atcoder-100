import sys
from collections import deque

data = sys.stdin.readlines()
items = [line.rstrip().split() for line in data]
n, q = items.pop(0)
que = deque()

for p in items:
  que.append(p)

time = 0

while que:
  p = que.popleft()
  p[1] = int(p[1]) - int(q)
  if (p[1] > 0):
    que.append(p)
    time += int(q)
  else:
    time += p[1] + int(q)
    print(f"{p[0]} {time}")
