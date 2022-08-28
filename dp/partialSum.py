n = int(input())
a = list(map(int, input().split()))
goal = int(input())

dp = [[False] * 10010 for _ in range(110)]

dp[0][0] = True

for i in range(n):
  for j in range(goal + 1):
    if (j >= a[i]):
      dp[i + 1][j] = dp[i][j - a[i]] or dp[i][j]
    else:
      dp[i + 1][j] = dp[i][j]

if (dp[n][goal]):
  print("YES")
else:
  print("NO")