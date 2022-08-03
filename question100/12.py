import sys
import copy


data = sys.stdin.readlines()
items = [list(map(int, line.rstrip().split())) for line in data]
n, m = items.pop(0)

family = {}

for i in items:
  x = i[0]
  y = i[1]
  if (x in family):
    family[x] = family[x] + [y]
  else:
    family[x] = [y]
  if (y in family):
    family[y] = family[y] + [x]
  else:
    family[y] = [x]

ans = 1

for bit in range(1 << n):
  friends = []
  for i in range(n):
    shift_i = 1 << i
    if bit & shift_i > 0:
      friends.append(i + 1)
  
  flag = True
  for f in friends:
    other = copy.copy(friends)
    other.remove(f)
    for o in other:
      if (not (f in family)): 
        flag = False
        continue
      if (o in family[f]): continue
      flag = False
  
  if (flag):
    ans = max([ans, len(friends)])

print(ans)