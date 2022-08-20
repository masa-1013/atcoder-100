import sys

data = sys.stdin.readlines()
a, b, c, d = [list(map(int, line.rstrip().split())) for line in data]
ans = []

for bit in range(1 << a[0]):
  number = 0
  for i in range(a[0]):
    shift_i = 1 << i
    if bit & shift_i > 0:
      number += b[i]
  if (number in d):
    ans.append(number)

for i in d:
  if (i in ans):
    print("yes")
  else:
    print("no")
