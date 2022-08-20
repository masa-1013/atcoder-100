import sys

data = sys.stdin.readlines()
items = [list(map(int, line.rstrip().split())) for line in data]
n = items.pop(0)

ans = 100000000000

for item in items:
  s = item[0]
  for j in items:
    e = j[1]
    total = 0
    for i in items:
      a = abs(i[0] - s)
      b = abs(i[1] - e)
      ab = abs(i[1] - i[0])
      total += (a + b + ab)
    ans = min([ans, total])

print(ans)
