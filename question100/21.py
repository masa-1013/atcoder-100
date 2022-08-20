n = int(input())
hs_list = [list(map(int, input().split())) for _ in range(n)]

def check(x):
  shooting_times= []
  for hs in hs_list:
    tmp = x - hs[0]
    if (tmp < 0):
      return False
    else:
      shooting_times.append(tmp // hs[1])
  
  t = 0
  for shooting_time in sorted(shooting_times):
    if (shooting_time >= t):
      t += 1
      continue

    return False
  
  return True


def search(left, right):
  if (right - left == 1):
    if (check(left)):
      return left
    else:
      return right

  index = (left + right) // 2
  reslust = check(index)

  if (reslust):
    right = index
  else:
    left = index

  return search(left, right)

print(search(1, 10**19))