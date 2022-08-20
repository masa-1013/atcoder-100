from collections import deque

r, c = list(map(int, input().split()))
start_y, start_x = list(map(int, input().split()))
goal_y, goal_x = list(map(int, input().split()))
maze = [list(input()) for _ in range(r)]
dist = [[-1] * c for _ in range(r) ]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
que = deque()
que.append([start_x - 1, start_y - 1])
dist[start_y - 1][start_x - 1] = 0

while que:
  current_x, current_y = que.popleft()
  for i in range(4):
    next_x = current_x + dx[i]
    next_y = current_y + dy[i]

    if (next_x < 0 or next_x >= c): continue
    if (next_y < 0 or next_y >= r): continue
    if (maze[next_y][next_x] == "#"): continue
    if (dist[next_y][next_x] != -1): continue

    dist[next_y][next_x] = dist[current_y][current_x] + 1
    que.append([next_x, next_y])

print(dist[goal_y - 1][goal_x - 1])