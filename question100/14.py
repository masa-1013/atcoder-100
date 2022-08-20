n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

ans = 100000000000000000

for bit in range(1 << n):
  bits = list(bin(bit)[2:].zfill(n))

  building = [0] * n
  max_h = a[0]
  money = 0
  for index, i in enumerate(bits):
    if (i == '0' or index == 0): 
      building[index] = a[index]
      max_h = max([max_h, a[index]])
      continue
    
    if (max_h >= a[index]):
      building[index] = max_h + 1
      money += (building[index] - a[index])
      max_h += 1
    else:
      building[index] = a[index]
      max_h = a[index]
  
  max_h = building[0]
  point = 0
  for index, i in enumerate(building):
    if (index == 0):
      point += 1
      continue

    if (i > max_h):
      point += 1
      max_h = i
  
  if (point >= k):
    ans = min([ans, money])

print(ans)