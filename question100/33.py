from collections import deque
import itertools


h, w = list(map(int, input().split()))
area = [list(input()) for _ in range(h)]
dist = [[-1] * w for _ in range(h)]

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
    if (area[next_y][next_x] == '#'): continue

    dist[next_y][next_x] = dist[current_y][current_x] + 1
    que.append([next_x, next_y])

goal = dist[h - 1][w - 1]

if (goal == -1):
  print(-1)
else:
  numberOfBlack = list(itertools.chain.from_iterable(area)).count('#')
  ans = (w * h) - goal - numberOfBlack
  print(ans)