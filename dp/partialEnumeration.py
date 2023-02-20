n = int(input())
a = list(map(int, input().split()))
goal = int(input())

MOD = 1000000009

dp = [[0] * 10010 for _ in range(110)]
dp[0][0] = 1

for i in range(n):
  for j in range(goal + 1):
    if (j >= a[i]):
      dp[i + 1][j] = dp[i][j - a[i]] + dp[i][j]
    else:
      dp[i + 1][j] = dp[i][j]

print(dp[n][goal])
