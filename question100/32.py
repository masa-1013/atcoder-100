from collections import deque

def execute():
  w, h = list(map(int, input().split()))
  if (w == 0 and h == 0): exit()

  maze = [list(map(int, input().split())) for _ in range(2 * h - 1)]
  dist = [[-1] * w for _ in range(h)]

  def existWall(current_x, current_y, dx, dy):
    ## X方向に壁が存在するか
    if (dx != 0):
      if (dx == 1):
        maze_x = current_x
      else:
        maze_x = current_x - 1
      
      maze_y = 2 * current_y

      if (maze_x < 0 or maze_x >= (w - 1)): return True
      return maze[maze_y][maze_x] == 1
    
    ## Y方向に壁が存在するか
    if (dy != 0):
      maze_x = current_x

      if (dy == 1):
        maze_y = 2 * current_y + 1
      else:
        maze_y = 2 * (current_y - 1) + 1

      if (maze_y < 0 or maze_y >= (2 * h - 1)): return True
      
      return maze[maze_y][maze_x] == 1

  que = deque()
  que.append([0, 0])
  dist[0][0] = 1

  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1]

  while que:
    current_x, current_y = que.popleft()
    for i in range(4):
      next_x = current_x + dx[i]
      next_y = current_y + dy[i]

      if (next_x < 0 or next_x >= w): continue
      if (next_y < 0 or next_y >= h): continue
      if (dist[next_y][next_x] != -1): continue
      if (existWall(current_x, current_y, dx[i], dy[i])): continue

      dist[next_y][next_x] = dist[current_y][current_x] + 1
      que.append([next_x, next_y])

  goal = dist[h - 1][w - 1]

  print(max([0, goal]))

while True:
  execute()