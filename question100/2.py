import sys

data = sys.stdin.readlines()
n = int([line.rstrip() for line in data][0])

def divisor(n):
  count = 0
  for i in range(1, int(n**0.5)+1):
    if (n % i == 0):
      count += 1
  
  return count * 2

ans = 0

for i in range(1, n+1):
  if (i % 2 == 0): continue
  if (divisor(i) == 8):
    ans += 1
  
print(ans)