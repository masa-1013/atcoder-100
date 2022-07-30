import sys

data = sys.stdin.readlines()
n, sortItems = [line.rstrip() for line in data]

n = int(n)
sortItems = [int(i) for i in sortItems.split(' ')]

for index, item in enumerate(sortItems):
  for j in reversed(list(range(0, index))):
    target = sortItems[j]
    if (target > item):
      sortItems[j+1] = target
      sortItems[j] = item
  print(' '.join(map(str, sortItems)))
