n, m = list(map(int, input().split()))
coins = list(map(int, input().split()))

dp = [[10000000000] * (n + 1) for _ in range(m + 1)]

for i in range(m + 1):
  for j in range(n + 1):
    if (j == 0): 
      dp[i][j] = 0
      continue
    if (i == 0): continue

    coins_value = coins[i - 1]
    if (n >= coins_value):
      dp[i][j] = min([dp[i - 1][j], dp[i][j - coins_value] + 1])
    else:
      dp[i][j] = dp[i - 1][j]

print(dp[m][n])