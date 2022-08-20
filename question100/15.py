import itertools

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n) ]
ways = itertools.permutations(range(n), n)

ans = 0
number = 0

for way in ways:
  number += 1
  total = 0
  for i in range(n-1):
    start = way[i]
    end = way[i+1]
    x = (xy[start][0] - xy[end][0])**2
    y = (xy[start][1] - xy[end][1])**2
    total += ((x + y)**0.5)
  
  ans += total

print(ans / number)