import sys

data = sys.stdin.readlines()
a, b, c, x, y = [list(map(int, line.rstrip().split())) for line in data][0]

ans = 0

if ((a+b) >= c*2):
  i = min([x, y])
  if (x > y):
    if (a > c*2):
      print(c*(max([x, y]))*2)
    else:
      print(c*i*2 + a*(x-i) + b*(y-i))
  else:
    if (b > c*2):
      print(c*(max([x, y]))*2)
    else:
      print(c*i*2 + a*(x-i) + b*(y-i))
else:
  print(a*x + b*y)