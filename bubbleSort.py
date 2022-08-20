import sys

data = sys.stdin.readlines()
n, sortItems = [line.rstrip() for line in data]

n = int(n)
sortItems = [int(i) for i in sortItems.split(' ')]
count = 0

for index, item in enumerate(sortItems):
  for j in range(n-1, index, -1):
    if (sortItems[j-1] > sortItems[j]):
      count += 1
      sortItems[j], sortItems[j-1] = sortItems[j-1], sortItems[j]

print(' '.join(map(str, sortItems)))
print(count)