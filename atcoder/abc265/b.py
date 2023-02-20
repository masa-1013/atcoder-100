n, m, t = list(map(int, input().split()))
move_costs = list(map(int, input().split()))
bonus_rooms = {}

for i in range(m):
  item = list(map(int, input().split()))
  bonus_rooms[item[0]] = item[1]

for index, move_cost in enumerate(move_costs):
  if ((index + 1) in bonus_rooms):
    t += bonus_rooms[index + 1]
  
  t -= move_cost
  if (t <= 0):
    print("No")
    exit()

print("Yes")
