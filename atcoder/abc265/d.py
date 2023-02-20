from bisect import bisect_left as bisect
import sys
sys.setrecursionlimit(10**9)

n, p, q, r = list(map(int, input().split()))
a = list(map(int, input().split()))

s = [0] * (n + 1)

for i in range(n):
  s[i + 1] = s[i] + a[i]

for i in range(n + 1):
  y_index = bisect(s, s[i] + p)
  if (y_index > n or s[y_index] != s[i] + p): 
    continue

  z_index = bisect(s, s[i] + p + q)
  if (z_index > n or s[z_index] != s[i] + p + q): 
    continue

  w_index = bisect(s, s[i] + p + q + r)
  if (w_index > n or s[w_index] != s[i] + p + q + r): 
    continue

  print("Yes")
  break
else:
  print("No")
