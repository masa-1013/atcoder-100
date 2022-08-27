s = list(input())

goal = ['a', 't', 'c', 'o', 'd', 'e', 'r']

change_count = 0
for index, i in enumerate(goal):
  if (s[index] == i): continue

  target_index = s.index(i)
  for j in reversed(range(index + 1, target_index + 1)):
    s[j], s[j - 1] = s[j - 1], s[j]
    change_count += 1
    if (s[index] == i): break

print(change_count)