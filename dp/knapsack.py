n = int(input())

weight = []
value = []

for i in range(n):
  item = list(map(int, input().split()))
  weight.append(item[0])
  value.append(item[1])

w = int(input())
dp = [[0] * 10010 for _ in range(110)]

for i in range(n):
  for j in range(w + 1):
    if (j >= weight[i]):
      dp[i + 1][j] = max(dp[i][j - weight[i]] + value[i], dp[i][j])
    else:
      dp[i + 1][j] = dp[i][j]

print(dp[n][w])