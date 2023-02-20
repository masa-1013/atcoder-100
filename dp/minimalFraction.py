n = int(input())
a = list(map(int, input().split()))
goal = int(input())

dp = [[100000] * 10100 for _ in range(110)]

dp[0][0] = 0

for i in range(n):
  for j in range(goal + 1):
    if (j >= a[i]):
      dp[i + 1][j] = min(dp[i][j - a[i]] + 1, dp[i][j])
    else:
      dp[i + 1][j] = dp[i][j]

print(dp[n][goal])