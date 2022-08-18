import bisect

n, m = list(map(int, input().split()))
p = [0] + [int(input()) for _ in range(n)]

two_points = []
for i in p:
  for j in p:
    two_points.append(i + j)

two_points.sort()

ans = 0

for i in two_points:
  if (i > m): break
  index = bisect.bisect_right(two_points, m - i) - 1
  ans = max([ans, two_points[index] + i])

print(ans)