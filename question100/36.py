n, w = list(map(int, input().split()))
weight = []
values = []

for _ in range(n):
  item = list(map(int, input().split()))
  values.append(item[0])
  weight.append(item[1])


dp = [[0] * (w + 1) for _ in range(n + 1)]

for i in range(n):
  for w in range(w + 1):
    ## i 番目の品物を選ぶ場合
    if (w - weight[i] >= 0):
      dp[i + 1][w] = max([dp[i][w], dp[i + 1][w - weight[i]] + values[i]])
    else:
      dp[i + 1][w] = dp[i][w]
    
print(dp[n][w])