import sys

data = sys.stdin.readlines()
data = [int(line.rstrip()) for line in data]

minScore = 1000000
result = -1000000

for r in data:
  result = max(result, r-minScore)
  minScore = min(minScore, r)

print(result)
