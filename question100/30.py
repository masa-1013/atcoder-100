from collections import deque

h, w, n = list(map(int, input().split()))
area = [list(input()) for _ in range(h)]
numbers = ["S"] + list(map(str, range(1,10)))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

number_to_index = {}
for y in range(h):
  for x in range(w):
    v = area[y][x]
    if (v in numbers):
      number_to_index[v] = [x, y]


def bfs(s, e):
  dist = [[-1] * w for _ in range(h)]
  que = deque()
  que.append([s[0], s[1]])
  dist[s[1]][s[0]] = 0

  while que:
    current_x, current_y = que.popleft()
    for i in range(4):
      next_x = current_x + dx[i]
      next_y = current_y + dy[i]

      if (next_x < 0 or next_x >= w): continue
      if (next_y < 0 or next_y >= h): continue
      if (area[next_y][next_x] == "X"): continue
      if (dist[next_y][next_x] != -1): continue

      dist[next_y][next_x] = dist[current_y][current_x] + 1
      que.append([next_x, next_y])

      if ([next_x, next_y] == e): return dist[next_y][next_x]

s = number_to_index["S"]
ans = 0
for i in list(map(str, range(1, n + 1))):
  e = number_to_index[i]
  v = bfs(s, e)
  ans += v
  s = e

print(ans)