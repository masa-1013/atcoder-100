from collections import deque

n = int(input())
items = [list(map(int, input().split())) for _ in range(n)]
graph = [[] for _ in range(n+1)]

for index, i in enumerate(items):
  if (i[1] == 0): continue
  for j in i[2:]:
    graph[index + 1].append(j)

dist = [-1] * (n + 1)
dist[0] = 0
dist[1] = 1

d = deque()
d.append(1)

while d:
  v = d.popleft()
  for i in graph[v]:
    if (dist[i] != -1): continue
    dist[i] = dist[v] + 1
    d.append(i)

ans = dist[1:]

for index, i in enumerate(ans):
  if (i == -1):
    print(f"{index + 1} {i}")
  else:  
    print(f"{index + 1} {i - 1}")