n = int(input())
items = [list(map(int, input().split())) for _ in range(n)]

times = 0
ans = [[0]*2 for _ in range(n)]
seen = [False] * n
graph = []
for i in items:
  if (i[1] == 0): 
    graph.append([])
  else:
    graph.append(i[2:])

def dfs(v):
  global times
  seen[v] = True
  times += 1
  ans[v][0] = times

  for next_v in graph[v]:
    if (seen[next_v - 1]): continue
    dfs(next_v - 1)
  
  times += 1
  ans[v][1] = times

for v in range(n):
  if (seen[v]): continue
  dfs(v)


for index, i in enumerate(ans):
  print(f"{index + 1} {i[0]} {i[1]}")