n, q = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(n-1)]
px = [list(map(int, input().split())) for _ in range(q)]
seen = [False] * n

ans = [0] * n
graph = [[] for _ in range(n)]
for i in ab:
  graph[i[0] - 1] += [i[1] - 1]
  graph[i[1] - 1] += [i[0] - 1]

for i in px:
  ans[i[0] - 1] += i[1]

que = [0]

while not len(que) == 0:
  item = que.pop()
  seen[item] = True

  for i in graph[item]:
    if (seen[i]): continue
    ans[i] += ans[item]
    que.append(i)

print(" ".join(map(str, ans)))
