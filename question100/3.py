import sys

data = sys.stdin.readlines()
n = [line.rstrip() for line in data][0]

count = 0
ans = 0

for i in n:
  if (i == 'A' or i == 'C' or i == 'G' or i == 'T'):
    count += 1
    ans = max([count, ans])
  else:
    count = 0

print(ans)