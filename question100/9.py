import sys

data = sys.stdin.readlines()
items = [list(map(int, line.rstrip().split())) for line in data]
m = int(items.pop(0)[0])

target = items[0:m]
all = items[m+1:]

p = target[0]

for i in all:
  x = i[0] - p[0]
  y = i[1] - p[1]
  flag = True
  for j in target:
    newX = j[0] + x
    newY = j[1] + y
    if ([newX, newY] in all): continue
    flag = False
  
  if (flag):
    print(f"{x} {y}")
    exit()
    