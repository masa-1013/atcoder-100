import sys

data = sys.stdin.readlines()
l1, r1, l2, r2 = [line.rstrip() for line in data][0].split(' ')

range1 = list(range(int(l1), int(r1)+1))
range2 = list(range(int(l2), int(r2)+1))

range1.extend(range2)
result = len(range1) - len(set(range1))

if (result >= 1):
  print(result - 1)
else:
  print(0)
