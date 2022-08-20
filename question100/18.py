n = int(input())
s = sorted(list(set(map(int, input().split()))))
q = int(input())
t = list(map(int, input().split()))

def two_part_search(value, left, right):
  if right - left == 1:
    return s[left] == value or s[right] == value

  index = (left + right) // 2

  if (value >= s[index]):
    return two_part_search(value=value, left= index, right=right)
  else:
    return two_part_search(value=value, left=left, right=index)

ans = 0
l = len(s)
for i in t:
  if (two_part_search(value=i, left=0, right=l)):
    ans += 1

print(ans)