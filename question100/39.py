n = int(input())
numbers = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(n)]
dp[0][0] = 1

for i in range(n - 1):
  num = numbers[i]
  for j in range(21):
    if (num + j <= 20 and i > 0):
      dp[i + 1][j] += dp[i][j + num]
    if (j - num >= 0):
      dp[i + 1][j] += dp[i][j - num]

print(dp[n - 1][numbers[n - 1]])