import sys
import itertools

data = sys.stdin.readlines()
items = [list(map(int, line.rstrip().split())) for line in data]
n, m = items.pop(0)

all = itertools.combinations(list(range(1, m+1)), 2)

ans = 0

for i in all:
  point = 0
  for j in items:
    one = j[i[0] - 1]
    two = j[i[1] - 1]
    point += max([one, two])
  ans = max([ans, point])

print(ans)