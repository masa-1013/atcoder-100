import sys

data = sys.stdin.readlines()
items = [list(map(int, line.rstrip().split())) for line in data]
n, m = items.pop(0)
p = items.pop()
ans = 0

for bit in range(1 << n):
  on = []
  flag = True
  for i in range(n):
    shift_i = 1 << i
    if bit & shift_i > 0:
      on.append(i + 1)
  for index, item in enumerate(items):
    onCount = 0
    for j in item[1:]:
      if (j in on): onCount += 1
    
    if (onCount % 2 != p[index]): flag = False
  
  if (flag): ans += 1

print(ans)