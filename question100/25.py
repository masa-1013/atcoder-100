import sys
sys.setrecursionlimit(10000)

def search():
  w, h = list(map(int, input().split()))
  if (w == 0 and h == 0): return False

  island = [list(map(int, input().split())) for _ in range(h)]

  ans = 0
  seen = [[False]* w for _ in range(h)]
  dx = [1,1,0,-1,-1,-1,0,1]
  dy = [0,1,1,1,0,-1,-1,-1]
  s = []

  def dfs(x, y):
    if (seen[y][x]): return False
    seen[y][x] = True
    if (island[y][x] == 0): return False

    for i in range(8):
      next_x = x + dx[i]
      next_y = y + dy[i]

      if (next_x < 0 or next_x >= w): continue
      if (next_y < 0 or next_y >= h): continue

      can_move = (not seen[next_y][next_x]) and (island[next_y][next_x] == 1)

      if (can_move):
        s.append([next_x, next_y])
      else:
        seen[next_y][next_x]
    
    while (len(s) > 0):
      next = s.pop()
      dfs(next[0], next[1])
    
    return True

  for y in range(h):
    for x in range(w):
      if (dfs(x, y)): ans += 1

  print(ans)

  return True

while (True):
  if (not search()): break