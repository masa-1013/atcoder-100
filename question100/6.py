import sys

data = sys.stdin.readlines()
items = [line.rstrip().split() for line in data]
n, s = items[0][0], items[1][0]

ans = 0

for i in range(0, 1000):
  number = str(i).zfill(3)
  searchStr = s
  flag = True
  for j in number:
    index = searchStr.find(j)
    if (index == -1): 
      flag = False
      break
    searchStr = searchStr[index+1:]
  
  if (flag): ans += 1

print(ans)
