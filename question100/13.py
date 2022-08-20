import sys
import copy

data = sys.stdin.readlines()
items = [list(map(int, line.rstrip().split())) for line in data]
r, c = items.pop(0)
ans = 0

for bit in range(1 << r):
  reverse = list(bin(bit)[2:].zfill(r))
  items_copy = copy.deepcopy(items)
  for index, item in enumerate(items_copy):
    if (reverse[index] == '0'): continue
    for index_j, j in enumerate(item):
      item[index_j] = (j + 1) % 2

  total = 0
  for i in range(c):
    c_total = 0
    for j in range(r):
      c_total += items_copy[j][i]
    total += max([c_total, r-c_total])
  
  ans = max([ans, total])

print(ans)