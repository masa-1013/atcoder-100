n, m = list(map(int, input().split()))
p = [0] + [int(input()) for _ in range(n)]

two_points = []
for i in p:
  for j in p:
    two_points.append(i + j)

two_points = sorted(list(set(two_points)))

def search(value, left, right):
  while(right > left):
    if (right - left == 1):
      left_value = two_points[left] + value
      right_value = two_points[right] + value

      if (right_value <= m): 
        return right_value
      else:
        return left_value

    index = (left + right) // 2
    index_value = two_points[index]

    if (index_value + value <= m):
      left = index
    else:
      right = index

two_points_len = len(two_points)

ans = 0

for i in two_points:
  if (i > m): break
  search_value = search(i, 0, two_points_len - 1)

  if (search_value > m): continue
  ans = max([ans, search_value])

print(ans)