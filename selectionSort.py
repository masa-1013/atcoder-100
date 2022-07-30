import sys

data = sys.stdin.readlines()
n, sortItems = [line.rstrip() for line in data]

n = int(n)
sortItems = [int(i) for i in sortItems.split(' ')]
count = 0

for index, item in enumerate(sortItems):
  minj = index
  for j in range(index, n):
    if (sortItems[minj] > sortItems[j]):
      minj = j
  sortItems[index], sortItems[minj] = sortItems[minj], sortItems[index]
  if (sortItems[index] != sortItems[minj]):
    count += 1

print(' '.join(map(str, sortItems)))
print(count)