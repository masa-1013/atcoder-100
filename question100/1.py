import sys
import itertools

data = sys.stdin.readlines()
items = [list(map(int, line.rstrip().split())) for line in data]

for item in items:
  if (item[0] == 0 and item[1] == 0): exit()
  all = itertools.combinations(list(range(1, item[0]+1)), 3)
  count = 0
  for c in all:
    if (sum(c) == item[1]):
      count += 1
  print(count)