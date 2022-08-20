n = int(input())
a_parts_list = sorted(list(map(int, input().split())))
b_parts_list = sorted(list(map(int, input().split())))
c_parts_list = sorted(list(map(int, input().split())))

a_parts_list_len = len(a_parts_list)
b_parts_list_len = len(b_parts_list)
c_parts_list_len = len(c_parts_list)

def search_left(parts, parts_list, left, right):
  if (parts_list[0] >= parts): return 0
  if (parts_list[-1] < parts): return right + 1

  while (right > left):
    if (right - left == 1):
      if parts_list[left] >= parts:
        return left
      elif parts_list[right] >= parts:
        return right
      else:
        return -1
    
    index = (left + right) // 2

    if (parts > parts_list[index]):
      left = index
    else:
      right = index

def search_right(parts, parts_list, left, right):
  if (parts_list[0] > parts): return 0
  if (parts_list[-1] <= parts): return right + 1

  while (right > left):
    if (right - left == 1):
      if parts_list[right] <= parts:
        return right + 1
      elif parts_list[left] <= parts:
        return right
      else:
        return -1
    
    index = (left + right) // 2

    if (parts >= parts_list[index]):
      left = index
    else:
      right = index

ans = 0

for b_parts in b_parts_list:
  a_parts_index = search_left(b_parts, a_parts_list, 0, a_parts_list_len - 1)
  c_parts_index = search_right(b_parts, c_parts_list, 0, c_parts_list_len - 1)

  ans += (a_parts_index * (c_parts_list_len - c_parts_index))

print(ans)