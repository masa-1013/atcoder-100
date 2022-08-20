n = int(input())

def execute():
  x = list(input())
  y = list(input())

  x_len = len(x)
  y_len = len(y)

  dp = [[0] * (x_len + 1) for _ in range(y_len + 1)]

  for i in range(y_len + 1):
    for j in range(x_len + 1):
      if (i == 0 or j == 0): continue

      dp[i][j] = max([dp[i - 1][j], dp[i][j - 1]])
      if (x[j - 1] == y[i - 1]):
        dp[i][j] = max([dp[i][j], dp[i - 1][j - 1] + 1])

  print(dp[y_len][x_len])

for _ in range(n):
  execute()


