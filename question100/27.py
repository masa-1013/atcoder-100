w = int(input())
h = int(input())
field = [list(map(int, input().split())) for _ in range(h)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
seen = [[0] * w for _ in range(h)]

ans = 0

def dfs(x, y, count):
  global ans
  if (not seen[y][x] == 0): return
  if (field[y][x] == 0): return
  seen[y][x] = count
  ans = max([ans, count])

  for i in range(4):
    next_x = x + dx[i]
    next_y = y + dy[i]

    if (next_x < 0 or next_x >= w): continue
    if (next_y < 0 or next_y >= h): continue

    if (field[next_y][next_x] == 0): continue
    if (not seen[next_y][next_x] == 0): continue

    dfs(next_x, next_y, count + 1)

for y in range(h):
  for x in range(w):
    dfs(x, y, 1)
    seen = [[0] * w for _ in range(h)]

print(ans)
