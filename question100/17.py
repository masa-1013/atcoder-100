import itertools

k = int(input())
rc = [list(map(int, input().split())) for _ in range(k)]
per = itertools.permutations(range(8), 8)
area = [[0]*8 for i in range(8)]

def can_place_queen(position):
  if (area[position[1]][position[0]] == 1): return False
  move_pattern = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
  area[position[1]][position[0]] = 1
  for i in range(1, 8):
    for move in move_pattern:
      next_x = position[0] + (move[0] * i)
      next_y = position[1] + (move[1] * i)

      if (next_x >= 0 and next_x < 8 and next_y >= 0 and next_y < 8):
        area[next_y][next_x] = 1
  
  return True

def print_answer(queen_places):
  for y in range(8):
    row = ""
    for x in range(8):
      if (queen_places[y] == x):
        row += "Q"
      else:
        row += "."
    print(row)

for queen_places in per:
  can_seek = True
  for i in rc:
    if (queen_places[i[0]] != i[1]):
      can_seek = False
      break
  
  if (not can_seek): continue

  area = [[0]*8 for i in range(8)]
  can_place = True
  for index, place in enumerate(queen_places):
    if (can_place_queen([place, index])): continue
    can_place = False
    break

  if (can_place):
    print_answer(queen_places)