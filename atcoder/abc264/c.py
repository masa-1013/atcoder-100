h1, w1 = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(h1)]
h2, w2 = list(map(int, input().split()))
b = [list(map(int, input().split())) for _ in range(h2)]

for i in range(1 << h1):
  for j in range(1 << w1):
    hvec = []
    wvec = []
  
    for k in range(h1):
      if (i & (1 << k) > 0): hvec.append(k)

    for k in range(w1):
      if (j & (1 << k) > 0): wvec.append(k)

    if (len(hvec) != h2 or len(wvec) != w2): continue

    match = True

    for k in range(h2):
      for l in range(w2):
        if (b[k][l] != a[hvec[k]][wvec[l]]):
          match = False
          break
    
    if (match):
      print("Yes")
      exit()

print("No")