n = int(input())
a = list(map(int, input().split()))

dp = [0] * 10010

for i in range(n):
  dp[i + 1] = max(dp[i] + a[i], dp[i])

print(dp[n]) 