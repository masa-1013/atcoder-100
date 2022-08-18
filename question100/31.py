import sys
sys.setrecursionlimit(10000)

w, h = list(map(int, input().split()))
area = [list(map(int, input().split())) for _ in range(h)]
dx_odd = [1, 1, 1, 0, -1, 0]
dy_odd = [-1, 0, 1, 1, 0, -1]
dx_even = [0, 1, 0, -1, -1, -1]
dy_even = [-1, 0, 1, 1, 0, -1]

seen = [[False] * w for _ in range(h)]

def dfs(x, y):
  if (area[y][x] == 1): return
  if (seen[y][x]): return
  seen[y][x] = True

  for i in range(6):
    if ((y + 1) % 2 == 0):
      dx = dx_even
      dy = dy_even
    else:
      dx = dx_odd
      dy = dy_odd

    next_x = x + dx[i]
    next_y = y + dy[i]

    if (next_x < 0 or next_x >= w): continue
    if (next_y < 0 or next_y >= h): continue
    if (seen[next_y][next_x]): continue
    if (area[next_y][next_x] == 1): continue

    dfs(next_x, next_y)

def count_light_on_true(x, y):
  if (not seen[y][x]): return 0

  total = 0
  for i in range(6):
    if ((y + 1) % 2 == 0):
      dx = dx_even
      dy = dy_even
    else:
      dx = dx_odd
      dy = dy_odd

    next_x = x + dx[i]
    next_y = y + dy[i]

    if (next_x < 0 or next_x >= w): continue
    if (next_y < 0 or next_y >= h): continue
    if (seen[next_y][next_x]): continue

    total += 1
  
  return total

def count_light_on_edge(x, y):
  if (seen[y][x]): return 0

  total = 0
  for i in range(6):
    if ((y + 1) % 2 == 0):
      dx = dx_even
      dy = dy_even
    else:
      dx = dx_odd
      dy = dy_odd

    next_x = x + dx[i]
    next_y = y + dy[i]

    if (next_x < 0 or next_x >= w or next_y < 0 or next_y >= h):
      total += 1
  
  return total

for y in range(h):
  for x in range(w):
    if (y == 0 or y == (h - 1)):
      dfs(x, y)
    else:
      if (x == 0 or x == (w - 1)):
        dfs(x, y)

ans = 0

for y in range(h):
  for x in range(w):
    ans += count_light_on_true(x, y)

for y in range(h):
  for x in range(w):
    if (y == 0 or y == (h - 1)):
      ans += count_light_on_edge(x, y)
    else:
      if (x == 0 or x == (w - 1)):
        ans += count_light_on_edge(x, y)

print(ans)