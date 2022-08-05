n = int(input())
a_parts_list = sorted(list(map(int, input().split())))
b_parts_list = sorted(list(map(int, input().split())))
c_parts_list = sorted(list(map(int, input().split())))

a_parts_list_len = len(a_parts_list)
b_parts_list_len = len(b_parts_list)
c_parts_list_len = len(c_parts_list)

def search_up(parts, parts_list, left, right):
  if (left == right): return left
  if (parts_list[0] > parts): return 0
  if (parts_list[-1] < parts): return -1

  while (right > left):
    if (parts_list[right] == parts): return right
    if (parts_list[left] == parts): return left

    if (right - left == 1):
      if parts_list[left] == parts:
        return left
      elif parts_list[right] >= parts:
        return right
      else:
        return -1
    
    index = (left + right) // 2

    if (parts >= parts_list[index]):
      left = index
    else:
      right = index

def search_down(parts, parts_list, left, right):
  if (left == right): return left
  if (parts_list[0] > parts): return -1
  if (parts_list[-1] < parts): return right

  while (right > left):
    if (parts_list[right] == parts): return right
    if (parts_list[left] == parts): return left

    if (right - left == 1):
      if parts_list[right] == parts:
        return right
      elif parts_list[left] <= parts:
        return left
      else:
        return -1
    
    index = (left + right) // 2

    if (parts >= parts_list[index]):
      left = index
    else:
      right = index

ans = 0

for b_parts in b_parts_list:
  a_parts_index = search_down(b_parts, a_parts_list, 0, a_parts_list_len - 1)
  if (a_parts_list[a_parts_index] == b_parts):
    a_parts_index -= 1
  if (a_parts_index < 0): continue

  c_parts_index = search_up(b_parts, c_parts_list, 0, c_parts_list_len - 1)
  if (c_parts_index == -1): continue
  if (c_parts_list[c_parts_index] == b_parts):
    c_parts_index += 1

  total = (a_parts_index + 1) * (c_parts_list_len - c_parts_index)
  ans += total

print(ans)