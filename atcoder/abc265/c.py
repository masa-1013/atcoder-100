h, w = list(map(int, input().split()))
g = [list(input()) for _ in range(h)]

seen = [[False] * w for _ in range(h)]
current_x = 0
current_y = 0

while True:
  if (seen[current_y][current_x]):
    print(-1)
    exit()

  seen[current_y][current_x] = True

  value = g[current_y][current_x]

  if (value == 'U' and (current_y + 1) != 1):
    current_y -= 1
  elif (value == 'D' and (current_y + 1) != h):
    current_y += 1
  elif (value == 'L' and (current_x + 1) != 1):
    current_x -= 1
  elif (value == 'R' and (current_x + 1) != w):
    current_x += 1
  else:
    print(f"{current_y + 1} {current_x + 1}")
    exit()